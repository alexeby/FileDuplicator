# File Duplicator

## Description
The purpose of this program is to easily create copies of files while populating the files with generated information - 
such as person or address information, random numbers, etc. This was developed for the purpose of bulk testing import
functionality of other programs - especially if that program relies on unique information when importing.

## Installation
This project is compatible with Python 3.6. To install all requirements use:<br>
`pip install -r requirements.txt`

On Windows, a build can be created by running `build.bat`. This uses Pyinstaller to create an executable file which 
allows for easy build distribution. Note that this batch file relies on the project installation to use a python 
virtual environment.

## Configurations

|Configuration|Description|Default Value|
|---|---|---|
|`original_file_dir`|Location of original file to copy|./in/|
|`copy_file_dir`|Location of copied files|./out/|
|`num_copies`|Number of copies to make|5|
|`api_url`|URL of API to generate random person data|https://randomuser.me/api/?nat=us&results=%(num_copies)s|
|`left_token_trim`|Left part of token to remove in result|{|
|`right_token_trim`|Right part of token to remove in result|}|
|`clear_copy_path`|When 'True', will delete all files in the specified copy_file_dir out path|True|
|`all_unique_persons`|When 'True', will generate a new person per {Person.\*} or {Address.\*}|False|

## Supported Token Operations

### Preliminary Information
Tokens specifying multiple Persons/Addresses per file. `{Person.FirstName}` and `{Person.FirstName}`
will generate the same name while `{Person.FirstName}`, `{PersonA.FirstName}`, and `{Person1B.FirstName}` will all 
generate different names. This is the same with address - `{Address.Street}` and `{Address2.Street}` will generate
different addresses.

Nested tokens can be used for more complex operations with generated data. For example: `{math.exp({number_formatter('X')})}`
returns Euler's number raised to a randomly generated number.

Token mappings (`{Person.MAPPING}`) can be given aliases by adding a word to the mapping within **mappings.ini** file.
Aliases should be added with the `|` delimiter separating them. For example: `postal_code = PostalCode|Zip|ZipCode`. 
Note that these mappings must be unique and are not case-sensitive.

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
|`{Person.Age}`|Age|
|`{Person.Gender}`|Gender|
|`{Person.Nat}`|Nationality|
|`{Person.Username}`|Username|
|`{Person.Password}`|Password|

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
|`{number_formatter(x_pattern)}`|Creates random numbers following X-Pattern.|
|`{generate_date(date_format, start_date, end_date)}`|Generates a random date. Default parameters are generate_date('%m/%d/%Y', '01/01/1970', 'NOW') where 'NOW' is the current datetime.|
|`{value(value_list)}`|Randomly selects a value from a list of string objects.|
|`{date_formatter(date, original_format, changed_format)}`|Takes a date with that date's format, then changes that date to the specified format.|
|`{scramble_string(string)}`|Scrambles the characters in a string randomly.|
|`{generate_string(length)}`|Generates a string from every letter of the alphabet. Takes a number parameter to specify length of string.|

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

## Example 1
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
Result of Example 1:
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

## Example 2:
```text
Person Data Test
First name: {Person.FirstName}
Middle Name: {Person.MiddleName}
Last name: {Person.LastName}
Full name: {Person.FullName}
Title: {Person.Title}
Tax ID: {Person.TaxId}
Birthdate: {Person.Birthdate}
Age: {Person.Age}
Gender: {Person.Gender}
Nationality: {Person.Nat}
Username: {Person.Username}
Password: {Person.Password}

Address Data Test
Street: {Address.Street}
City: {Address.City}
State: {Address.State}
Postal code: {Address.PostalCode}
Country: {Address.Country}
Home phone: {Address.HomePhone}
Mobile phone: {Address.MobilePhone}
Email: {Address.Email}
Latitude: {Address.Latitude}
Longitude: {Address.Longitude}

Another Person Data Test
First name: {Person2.FirstName}
Middle Name: {Person2.MiddleName}
Last name: {Person2.LastName}
Full name: {Person2.FullName}
Title: {Person2.Title}
Tax ID: {Person2.TaxId}
Birthdate: {Person2.Birthdate}
Age: {Person2.Age}
Gender: {Person2.Gender}
Nationality: {Person.Nat}
Username: {Person2.Username}
Password: {Person2.Password}

Another Address Data Test
Street: {Address2.Street}
City: {Address2.City}
State: {Address2.State}
Postal code: {Address2.Zip}
Country: {Address2.Country}
Home phone: {Address2.HomePhone}
Mobile phone: {Address2.MobilePhone}
Email: {Address2.Email}
Latitude: {Address2.Latitude}
Longitude: {Address2.Longitude}

Number Formatter Test
XXX-XXX-XXXX: {number_formatter('XXX-XXX-XXXX')}
My Age is 2X: {number_formatter('My Age is 2X')}

Date Generator Test
Default: {generate_date()}
T format: {generate_date('%Y-%m-%dT%H:%M:%S')}
Future date: {generate_date('%m/%d/%Y', 'NOW', '01/01/2030')}

Random Values Test
YNU: {value(['YES', 'NO', 'UNK'])}

String Scrambler Test
Password: {scramble_string('Password')}

String Generator Test
10 Characters long: {generate_string(10)}

Nested Token Test
Number Formatter and Scramble String: {number_formatter('{scramble_string('XXX-XXX-XXXX')}')}
Reformat Date: {date_formatter('{Person.dob}', '%Y-%m-%dT%H:%M:%S.%fZ', '%Y/%m/%d')}
Reformat Date with inline token: {Person2.FirstName} was born on {date_formatter('{Person2.dob}', '%Y-%m-%dT%H:%M:%S.%fZ', '%m/%d/%Y')}
```
Result of Example 2:
```text
Person Data Test
First name: Theresa
Middle Name: anobGhsrseieT
Last name: Gibson
Full name: Theresa Gibson
Title: Miss
Tax ID: 564-46-3125
Birthdate: 1957-09-11T00:16:00.624Z
Age: 64
Gender: F
Nationality: US
Username: bigbutterfly460
Password: herbert

Address Data Test
Street: 6232 Marsh Ln
City: Sunnyvale
State: GA
Postal code: 65036
Country: United States
Home phone: (062)-833-0507
Mobile phone: (516)-941-6016
Email: theresa.gibson@example.com
Latitude: 57.9948
Longitude: -56.7348

Another Person Data Test
First name: Leroy
Middle Name: lSraeiLvyo
Last name: Silva
Full name: Leroy Silva
Title: Mr
Tax ID: 809-81-4821
Birthdate: 1984-05-17T16:16:27.317Z
Age: 37
Gender: M
Nationality: US
Username: bluerabbit147
Password: toolbox

Another Address Data Test
Street: 159 E Sandy Lake Rd
City: Pasadena
State: HI
Postal code: 81428
Country: United States
Home phone: (031)-582-6620
Mobile phone: (956)-437-4839
Email: leroy.silva@example.com
Latitude: 77.1729
Longitude: -38.9795

Number Formatter Test
XXX-XXX-XXXX: 211-892-8955
My Age is 2X: My Age is 28

Date Generator Test
Default: 08/24/2010
T format: 1995-08-30T01:28:55
Future date: 01/03/2025

Random Values Test
YNU: NO

String Scrambler Test
Password: Pasdowsr

String Generator Test
10 Characters long: mujrcmleut

Nested Token Test
Number Formatter and Scramble String: 8777559-8-00
Reformat Date: 1957/09/11
Reformat Date with inline token: Leroy was born on 05/17/1984
```

## Release Notes
|Release|Date|Notes|
|---|---|---|
|1.0.0|02/17/2021|+ Initial release|
|1.0.1|03/04/2021|+ Fixed issue where application would not run on Windows 10 due to Windows Defender and Pyinstaller incompatibility|
|1.0.2|03/05/2021|+ Added better error handling for invalid tokens<br>+ Improved naming convention of copied files|
|2.0.0|03/18/2021|+ Added file pre-execution file validation<br>+ Added support for nested tokens<br>+ Added support for multiple unique persons and addresses to be generated per file<br>+ Added `clear_copy_path` configuration, when `True` the file output directory will have its contents deleted<br>+ Added support for custom mapping values specified in `mappings.ini`<br>+ Added additional person mappings from API including `Username` and `Password`<br>+ Added date_formatter, generate_string, and scramble_string functions<br>+ Added ability to generate all person and address tokens uniquely - specified when `all_unique_persons` configuration is `True`. This will cause multiple uses of `{Person.FirstName}` to generate a different name rather than the same as when `all_unique_persons` is `False`<br><br>- Removed `regex_pattern` configuration. Nested token support removed token validation with regex|
|2.0.1|06/11/2021|+ Added stdout of files being created to better show progress<br>+ Added number iterator to create unique data. Useful for large data sets<br>+ Fixed bug where infinite loop could occur if no {Person} tag was used in the file|
