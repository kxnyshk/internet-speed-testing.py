# speedtest.net.py
A .py script to analyze the user's device internet download/upload speed and the ping receiving time, using speedtest.net's **`speedtest-cli`** PyPI library.

## Fetching the repo
 - Download the .zip file from [**here**](https://github.com/kxnyshk/speedtest.net.py/archive/refs/heads/master.zip)
 - Unzip/extract the dir
 - Open the extracted directory in VsCode or any other IDE of your choice.

## How to execute
 - Open the [**`app.py`**](https://github.com/kxnyshk/speedtest.net.py/blob/master/app.py) file in your IDE
 - Execute it in the terminal
   
   ### Requirements
    - Make sure you have [**speednet's**](https://www.speedtest.net/) [**`speedtest-cli`**](https://pypi.org/project/speedtest-cli/) PyPI library installed, if not, (in your terminal) do:
     - **`pip install speedtest-cli`**
      
## Results
 - The application with fetch all the nearest Servers based on the location
 - The best Server will be selected to perform the speed tests
 - Download/Upload speed (Mbits/s) will be displayed once done, followed by
 - The ping receiving time (ms)

## Demo Run
![image](https://user-images.githubusercontent.com/62258905/166065993-c49b7833-a215-4904-803e-c58fa44a7724.png)
