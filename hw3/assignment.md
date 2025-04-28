The goal is to get practical experience with creating a web service.

Your task is to create a REST service that will return:
- the actual temperature on a given international airport (in degrees of celsius)
- the actual price of a given stock
- evaluation of an arithmetic expression

The REST service will recognize three query string parameters, where exactly one of the three should be present (otherwise the service can return undefined value):
- queryAirportTemp - the IATA code of the airport (tree letters) for which to return the temperature 
- queryStockPrice - the identifier of the stock (1-4 letters) for which to get return the price
- queryEval - arithmetic expressions that can contain integer constants, parenthesis, and operations +, -, *, /

The result should be a JSON or XML document, which contains the result value. That is, the JSON return value should be the number value itself. In the case of the XML the value will be enclosed to some root tag, e.g. <result>10</result>. The content-type of the result must be always specified correctly (application/json, application/xml, or text/xml).

The service to test your homework runs at the URL address:
http://andromeda.fi.muni.cz/~xbatko/homework3
Run your web service on a web server (you can use a virtual computer in cloud.metacentrum.cz, any faculty computer such as aisa.fi.muni.cz, or any other public service). Use the above URL address with "email" and "url" query parameters. The "url" should be the URL for accessing your REST service, the "email" is your IS MUNI email, e.g. uco@mail.muni.cz. You will receive "OK", if the homework is successfuly submitted or some textual error, if there was a problem with your solution.

After the success result is received, submit the zipped source code of your solution to the IS depository.


Notes:
Stock prices can be, for example, retrieved using the Yahoo Finance API, the description of which can be found here:
https://rapidapi.com/apidojo/api/yahoo-finance1.
But there are other services, you can use ProgrammableWeb search engine to look for them:
http://www.programmableweb.com/category/financial/api

Actual weather information can be, for example, retrieved from AccuWeather:
http://apidev.accuweather.com/developers/
Of course, you can again search for any other service.

For information about the airports, you can use the following service:
http://www.airport-data.com/api/doc.php#airport

For the evaluation of the arithmetic expression, you can use any support library (e.g. Commons EL in Java). Note that even though the expression only contains integer constants the result might be a real number due to division.