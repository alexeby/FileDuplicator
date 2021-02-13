# FileDuplicator README

## Description

## Installation


## Configurations

|Configuration|Description|Default Value|
|---|---|---|
|`original_file_dir`|Location of original file to copy|./in/|
|`copy_file_dir`|Location of copied files|./out/|
|`num_copies`|Number of copies to make|5|
|`regex_pattern`|Regular expression of token|{.+?}|
|`api_url`|URL of API to generate random person data|https://randomuser.me/api/?nat=us&results=%(num_copies)s|
|`left_token_trim`|Left part of token to remove in result|{|
|`right_token_trim`|Right part of token to remove in result|}|

## Supported Token Operations

### Randomly Generated Person Data
|Token|Description|
|---|---|
|`Person.FirstName`|First Name|
|`Person.MiddleName`|Middle Name|
|`Person.LastName`|Last Name|
|`Person.FullName`|Full Name|
|`Person.Title`|Title|
|`Person.TaxID`|Tax ID|
|`Person.Birthdate`|Birthdate|
|`Person.Gender`|Gender|

### Randomly Generated Address Data
|Token|Description|
|---|---|
|`Address.Street`||
|`Address.City`||
|`Address.State`||
|`Address.PostalCode`||
|`Address.Country`||
|`Address.HomePhone`||
|`Address.MobilePhone`||
|`Address.Email`||
|`Address.Latitude`||
|`Address.Longitud`||

### Formatter Functions
|Token Example|Description|
|---|---|
|`number_formatter(X_Pattern)`|Creates random numbers following X-Pattern.|
|`generate_date(Date_Format, Start_Date, End_Date)`|Generates a random date. Default parameters are generate_date('%m/%d/%Y', '01/01/1970', 'NOW') where 'NOW' is the current datetime.|
|`value(Value_List)`|Randomly selects a value from a list of string objects.|

## Example
Example of how to use tokens to procedurally generate data:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<SampleFormat CreatedDate="">
    <Person FirstName="{Person.FirstName}" MiddleName="{Person.MiddleName}" LastName="{Person.LastName}" FullName="{Person.FullName}" Title="{Person.Title}" SSD="{Person.TaxID}" DOB="{Person.Birthdate}" Sex="{Person.Gender}">
        <Address Street="{Address.Street}" City="{Address.City}" State="{Address.State}" Zip="{Address.PostalCode}" Country="{Address.Country}" HomePhone="{Address.HomePhone}" MobilePhone="{Address.MobilePhone}" Email="{Address.Email}" Lat="{Address.Latitude}" Long="{Address.Longitude}" />
        <Information HaveChildren="{value(['Yes', 'No', 'Unknown'])}" NetWorth="{number_formatter('$X,XXX,XXX')}" DateLicenseReceived="{generate_date()}">
            <Vehicle Make="{value(['BMW', 'Audi', 'VW','Tesla'])}" Year="{generate_date('%Y')}" Mileage="{number_formatter('1XXXXX')}" />
        </Information>
    </Person>
</SampleFormat>
```
Result of the above example:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<SampleFormat CreatedDate="">
    <Person FirstName="Erin" MiddleName="ErinSoto" LastName="Soto" FullName="Erin Soto" Title="Miss" SSD="017-62-9920" DOB="1967-10-27T21:32:26.420Z" Sex="F">
        <Address Street="4821 Lovers Ln" City="Warren" State="ND" Zip="45755" Country="United States" HomePhone="(764)-664-4629" MobilePhone="(698)-446-1189" Email="erin.soto@example.com" Lat="41.3401" Long="149.0217" />
        <Information HaveChildren="Yes" NetWorth="$6,393,399" DateLicenseReceived="08/17/1975">
            <Vehicle Make="Audi" Year="2002" Mileage="197707" />
        </Information>
    </Person>
</SampleFormat>
```