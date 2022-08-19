Script that reads stdin line by line and computes metrics:

Input format: 
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), the statistics from the beginning will be printed:
        Total file size: File size: <total size>
        where <total size> is the sum of all previous <file size>
        Number of lines by status code:
            Possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            If a status code doesn’t appear or is not an integer, anything will be printed for this status code
            Format: <status code>: <number>
            Status codes will be printed in ascending order
