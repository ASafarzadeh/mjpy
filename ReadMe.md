[![Stargazers][stars-shield]][stars-url]
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mjpy?style=for-the-badge)
![PyPI - Status](https://img.shields.io/pypi/status/mjpy?style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/mjpy?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/mjpy?style=for-the-badge)
<br>


<div align="center">
<pre>                                                                                              
         _   ___       
  /\/\  (_) / _ \_   _ 
 /    \ | |/ /_)/ | | |
/ /\/\ \| / ___/| |_| |
\/    \// \/     \__, |
      |__/       |___/ </pre>
  <h1 align="center">MjPy(Temporarily stopped)</h1>

  <p align="center">
    An unofficial Midjourney client</a>
    <br>
  </p>
</div>



### Quick start
```
pip install mjpy
```
```
mjpy "cute cats playing football" -ch YOUR_CHANNEL_ID -g YOUR_GUILD_ID -t YOUR_TOKEN
```

### Installation

MjPy can be easily installed by pip using:
```
pip install mjpy
```
*The pip way is recommended because it adds the script to the path automatically in mac and linux, and installs the needed dependencies automatically.*
<br>
or you can use it using git clone command:

```
git clone https://github.com/ASafarzadeh/mjpy
```
The pip way does all the installations for you, but in the git clone way you should install the dependencies if they arent already installed. Mjpy depends on `requests` python module.<br><br>
You can install that with the command below:
```
python -m pip install requests
```
<br>Now you can navigate to Mjpy directory, and use it as the example below:
```
python mjpy.py "cute cats playing football" -ch YOUR_CHANNEL_ID -g YOUR_GUILD_ID -t YOUR_TOKEN
```



<!-- USAGE EXAMPLES -->
## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
prompt        |               | The prompt to be used if the command is imagine
-g            | --guild-id    | Your GUILD_ID
-c            | --channel-id  | Your CHANNEL_ID
-t            | --token       | Your Authorization_Token
-v            | --verbose     | Enable Verbosity and display the process in realtime(Default: False)
-o            | --output-dir  | Where to save the Generated images(Default: current dir(.))
-h            | --help        | show the help message and exit

<!-- CONTRIBUTING -->
## Contributing

Any contributions you make are **greatly appreciated**!

If you have a suggestion that would make MjPy better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

MjPy is Distributed under the GNU GPL license. take a look at the [LICENSE](https://github.com/ASafarzadeh/mjpy/blob/master/LICENSE) for more information.

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ASafarzadeh/mjpy.svg?style=for-the-badge
[contributors-url]: https://github.com/ASafarzadeh/mjpy/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ASafarzadeh/mjpy.svg?style=for-the-badge
[forks-url]: https://github.com/ASafarzadeh/mjpy/network/members
[stars-shield]: https://img.shields.io/github/stars/ASafarzadeh/mjpy.svg?style=for-the-badge
[stars-url]: https://github.com/ASafarzadeh/mjpy/stargazers
[issues-shield]: https://img.shields.io/github/issues/ASafarzadeh/mjpy.svg?style=for-the-badge
[issues-url]: https://github.com/ASafarzadeh/mjpy/issues
[license-shield]: https://img.shields.io/github/license/ASafarzadeh/mjpy.svg?style=for-the-badge
[license-url]: https://github.com/ASafarzadeh/mjpy/blob/master/LICENSE.txt
