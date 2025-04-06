The goal of this assignment is to get experience with W3C Web Service technology.

You can find a web service (using W3C standard) that simulates stock market at URL:
http://andromeda.fi.muni.cz/~xbatko/homework2

Use function createAccount to create your trading account, use your university email (uco@mail.muni.cz) so that the successful completion of the assignment will be assigned to you. As a return value from the createAccount method, you will receive a unique identifier that serves as auth token for the other methods.

Your goal is to trade (buy and sell) any stocks at this market in such a way that you double your initial account "money". In case you want to start again (with the initial amount), call the createAccount again to obtain a new auth token (note that this will make the previous one unusable).

The stock market is open 24/7.

After successful completion of the homework, submit your zipped source codes to IS depository https://is.muni.cz/auth/el/1433/jaro2025/PA053/ode/ode_hw2/. You will obtain the assignment points only if both the successful completion of the assingment is logged for your email and the source codes are submitted to IS.