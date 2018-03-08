# REPORTING TOOL

Connect our 1st and 3rd party data into one intuitive interface.

## How to Use
Run the web app through app.py. Debug mode is on currently.

# NEXT STEPS
  * Rewrite SAS workflow as OO design. Keep it modular, but stick to essentials
  * Build front-end workflow. May involve ajax.

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
    - type


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
      * Campaign   //default None
      * Flights[]  //default None

    - sasReportId
    - sasReportStatus // while loop when reportStatus != 200
    - sasReportFile

    * returnSASParameters()
    * returnDCMParameters()


  * Payload
    //Data to be sent to templates or to JS functions
    - dict


## HIGH LEVEL WORKFLOW
  * User specifies report parameters
  * Server looks up advertiser data
    - getSASID()
    - bool is 3rd Party Advertiser?
      - get3rdPartyType()
  * Construct SAS report parameters
  * createSASReport(); return jobID
  * retrieveSASReport()
  * downloadSASReport()
  * parseSASReport(); return performance, [(sasPlacementName, dcmPlacementID)]
  * construct DCM Report Parameters
  * create DCM Report
  * run DCM Report
  * find DCM report File
  * download DCM report
  * parse DCM report file; return performance
  * send results to HTML file








## Documentation

### DCM API

Edit reports by modifying (PATCHing) API objects - https://developers.google.com/doubleclick-advertisers/performance#patch

Create and update reports - https://developers.google.com/doubleclick-advertisers/guides/create_reports

Try using synchronous reports to retrieve data - https://developers.google.com/doubleclick-advertisers/guides/synchronousreports

Docs = https://developers.google.com/doubleclick-advertisers/getting_started
Authorization reference = https://developers.google.com/doubleclick-advertisers/authorizing

Dimension values (querying for specific info) - https://developers.google.com/doubleclick-advertisers/v3.0/dimensions
