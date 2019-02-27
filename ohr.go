package main

import (
	"bytes"
	"emis/clinical/payloads"
	"encoding/json"
	"encoding/xml"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

type openHrEvent struct {
	Id             string     `xml:"id"`
	PersonId       string     `xml:"patient"`
	EventType      string     `xml:"eventType"`
	EffectiveDate  openHrDate `xml:"effectiveTime"`
	IssueDate      string     `xml:"availabilityTimeStamp"`
	Code           openHrCode `xml:"code"`
	AssociatedText string     `xml:"associatedText"`
}

type openHRObservation struct {
	Episodicity string                 `xml:"episodicity"`
	Value       openHRObservationValue `xml:"value"`
}

type openHRObservationValue struct {
	Numeric openHRObservationNumericValue `xml:"numeric"`
}

type openHRObservationNumericValue struct {
	Quantification float32 `xml:"value"`
	Units          string  `xml:"units"`
}

type associatedText struct {
	Type  string `xml:"associatedTextType,attr"`
	Value string `xml:"value"`
}

type openHrDate struct {
	DatePart string `xml:"datepart,attr"`
	Value    string `xml:"value,attr"`
}

type openHrCode struct {
	Term         string            `xml:"displayName,attr"`
	SourceScheme string            `xml:"codeSystem,attr"`
	SourceCode   string            `xml:"code,attr"`
	Translation  openHrTranslation `xml:"translation"`
}

type openHrTranslation struct {
	CodeId string `xml:"code,attr"`
}

type authenticationResponse struct {
	token string
}

func main() {

	xmlStream, err := os.Open("c:\\emis\\openhr\\2ea56280-6e4b-4ec7-bab7-c5738a234280.xml")
	if err != nil {
		log.Println("Failed to open XML file")
		return
	}
	defer xmlStream.Close()

	decoder := xml.NewDecoder(xmlStream)
	for {
		// Read tokens from the XML document in a stream.
		t, _ := decoder.Token()
		if t == nil {
			break
		}

		switch se := t.(type) {
		case xml.StartElement:
			if se.Name.Local == "event" {
				var event openHrEvent
				decoder.DecodeElement(&event, &se)
				code := payloads.Code{
					SourceCodeId: event.Code.SourceCode,
					SourceScheme: event.Code.SourceScheme,
					Term:         event.Code.Term,
					CodeId:       event.Code.Translation.CodeId}

				request := payloads.AddRecordRequest{
					PersonId:      fmt.Sprintf("emis:person:%s", event.PersonId),
					RecordId:      fmt.Sprintf("emis:clinical:%s:%s", strings.ToLower(event.EventType), event.Id),
					EffectiveDate: FormatPartialDate(event.EffectiveDate.DatePart, event.EffectiveDate.Value),
					IssueDate:     fmt.Sprintf("ymdt:%s", event.IssueDate),
					Code:          code}

				api.client.AddObservation(request)

				jsonRequest, _ := json.Marshal(&request)
				if event.EventType == "XX" {
					log.Println(string(jsonRequest))
					log.Println()
				}
			}
		default:
		}
	}
}

func CallEndPoint(endPoint string, payload []byte, target interface{}) error {
	r, err := http.Post("http://localhost:5000/"+endPoint, "application/json", bytes.NewBuffer(payload))
	if err != nil {
		log.Println(err)
		return err
	}
	defer r.Body.Close()

	return json.NewDecoder(r.Body).Decode(target)
}

func FormatPartialDate(datepart string, date string) string {
	if datepart == "Y" {
		return "y:" + date[0:4]
	} // 2019
	if datepart == "YM" {
		return "ym:" + date[0:7]
	} // 2019-02
	if datepart == "YMD" {
		return "ymd:" + date[0:10]
	} //2019-02-14
	if datepart == "YMDT" {
		return "ymdt:" + date[0:15]
	} //2019-02-14T09:00

	return ""
}
