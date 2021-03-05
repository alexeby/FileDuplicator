# File Duplicator

## Description
The purpose of this program is to easily create copies of files while populating the files with generated information - 
such as person or address information, random numbers, etc. This was developed for the purpose of bulk testing import
functionality of other programs - especially if that program relies on unique information when importing.

## Installation
This project is compatible with Python 3.6. To install all requirements use:<br>
`pip install -r requirements.txt`

On Windows, a build can be created by running `build.bat`. This uses pyinstaller to create an executable file which 
allows for easy build distribution. Note that this batch file relies on the project installation to use a python 
virtual environment.

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
|`{Person.FirstName}`|First Name|
|`{Person.MiddleName}`|Middle Name|
|`{Person.LastName}`|Last Name|
|`{Person.FullName}`|Full Name|
|`{Person.Title}`|Title|
|`{Person.TaxID}`|Tax ID|
|`{Person.Birthdate}`|Birthdate|
|`{Person.Gender}`|Gender|

### Randomly Generated Address Data
|Token|Description|
|---|---|
|`{Address.Street}`|Street|
|`{Address.City}`|City|
|`{Address.State}`|State|
|`{Address.PostalCode}`|Postal Code|
|`{Address.Country}`|Country|
|`{Address.HomePhone}`|Home Phone|
|`{Address.MobilePhone}`|Mobile Phone|
|`{Address.Email}`|Email Address|
|`{Address.Latitude}`|Latitude|
|`{Address.Longitude}`|Longitude|

### Formatter Functions
|Token Example|Description|
|---|---|
|`{number_formatter(X_Pattern)}`|Creates random numbers following X-Pattern.|
|`{generate_date(Date_Format, Start_Date, End_Date)}`|Generates a random date. Default parameters are generate_date('%m/%d/%Y', '01/01/1970', 'NOW') where 'NOW' is the current datetime.|
|`{value(Value_List)}`|Randomly selects a value from a list of string objects.|

### Additional Packages and Resources
Additional supported packages:

|Package|Link|Example|
|---|---|---|
|`math`|https://docs.python.org/3/library/math.html|math.ceil(123.456)|
|`random`|https://docs.python.org/3/library/random.html|random.randint(0,20)|

Common Date Codes for Formatting:

| Code | Description |
|---|---|
|`%d`|Day|
|`%m`|Month|
|`%Y`|Year|
|`%H`|Hour|
|`%M`|Minute|
|`%S`|Second|
|`%f`|Microsecond|

_For more date codes please refer to https://www.w3schools.com/python/python_datetime.asp_

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