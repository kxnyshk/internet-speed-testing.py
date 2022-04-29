# LIB IMPORTS
import speedtest

# PATH IMPORTS
from paths import MODE
from paths import PATH_BEST
from paths import PATH_TEST
from paths import PATH_FETCH
from paths import PATH_FOUND
from paths import PATH_DOWN
from paths import PATH_UPLD

# INSTANCE
TEST = speedtest.Speedtest()

# FETCHING SERVERS
def fetchServers():
    f = open(PATH_FETCH, MODE)
    print(f.read())
    return TEST.get_servers()

# GETTING BEST SERVER
def getBestServer():
    f = open(PATH_BEST, MODE)
    print(f.read())
    return TEST.get_best_server()

def displayBestServer():
    DATA = getBestServer()
    HOST = DATA['host']
    CITY = DATA['name']
    CNTY = DATA['country']
    
    f = open(PATH_FOUND, MODE)
    print(f'{f.read()}{HOST} at {CITY}, {CNTY}')

# PERFORMING TESTS
def perfSpeedTests():
    f = open(PATH_TEST, MODE)
    print(f.read())

def perfDownload():
    f = open(PATH_DOWN, MODE)
    print(f.read())
    print(f'Download speed: {TEST.download() / 1024 / 1024:.2f} Mbit/s')

def perfUpload():
    f = open(PATH_UPLD, MODE)
    print(f.read())
    print(f'Upload speed: {TEST.upload() / 1024 / 1024:.2f} Mbit/s')

def pingResults():
    print(f'\nPing: {TEST.results.ping} ms')

# MAIN
def main():
    fetchServers()
    displayBestServer()
    perfSpeedTests()
    perfDownload()
    perfUpload()
    pingResults()

# RUN
# main()