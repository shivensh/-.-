from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" type="text/css" href="">
    <titleSudoR2spr Repository</title>
	<link rel="icon" type="image/x-icon" href="">

</head>

<body>
    <div class="container" style="bg-dark text-red text-center py-3 mt-5">
        <a href="https://github.com/shivensh" class="card">
            <p>
              />𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®❤️/>
                                             <br>

                <b>v2.0.0</b>
            </p>
        </a>
    </div>
	<br></br><br></br><br></br>
	<footer class="bg-dark text-white text-center py-3 mt-5">
	<center><img loading="lazy" class="object-none object-center" src="" width="40" height="40">
        Powered By 𝐈𝐓'𝐬𝐆𝐎𝐋𝐔.™®❤️ 
		<img loading="lazy" class="object-none object-center" src="" width="40" height="40">
		<div class="footer__copyright">
            <p class="footer__copyright-info">
                © 2024 Video Downloader. All rights reserved.
            </p>
        </div>
    </footer></center>
</body>

</html>
"""


if __name__ == "__main__":
    app.run()
