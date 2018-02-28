# REPORTING TOOL

Connect our 1st and 3rd party data into one intuitive interface.

## How to Use
Run the web app through app.py. Debug mode is on currently.

## ISSUES
  * Fail-safe when 3rd party data is not found
  * Ajax - get list of flights associated with campaign
  * Confirm tool can parse different creative templates
  * Refactor code so as not to be a complete mess


# Objects, Methods, and Attributes
  * dfareporting_utils
    - self-contained pieces. Avoid digging into this for as long as possible

  * 3rdPartyAccount
    - login()
    -

  * Advertiser
    - sasName
    - sasID
    - 3rdPartyID //default to None

  * Campaign
    - Flights []
    - Advertiser
    - sasID


  * Flight
    - startDate
    - endDate
    - Impression Goal
    - Impressions Served
    - Clicks
    - CTR

  * File
    - extension/filetype
    - filepath
    - parse()
    - Accumulate/reduce()
    - returnID()

  * Report
    - parameters
      * sasAdvertiser
      * startDate
      * endDate
      * Campaign //default None
      * Flights [] //default None

    - sasReportId
    - sasReportStatus // while loop when reportStatus != 200
    - sasReportFile

  * Payload
    //Data to be sent to templates or to JS functions
    - dict








## Documentation

### DCM API

Edit reports by modifying (PATCHing) API objects - https://developers.google.com/doubleclick-advertisers/performance#patch

Create and update reports - https://developers.google.com/doubleclick-advertisers/guides/create_reports

Try using synchronous reports to retrieve data - https://developers.google.com/doubleclick-advertisers/guides/synchronousreports

Docs = https://developers.google.com/doubleclick-advertisers/getting_started
Authorization reference = https://developers.google.com/doubleclick-advertisers/authorizing

Dimension values (querying for specific info) - https://developers.google.com/doubleclick-advertisers/v3.0/dimensions