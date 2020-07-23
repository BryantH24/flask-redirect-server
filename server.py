from flask import Flask, redirect, request

app = Flask(__name__)

#pulseM = "http://127.0.0.1:5000/?site=pulseM&fbuy_ref_code=bryant"
#mosquitosquad = "http://127.0.0.1:5000/?site=mosquito&fbuy_ref_code=bryant"
#pronto = "http://127.0.0.1:5000/?site=pronto&fbuy_ref_code=pulseM_referral_code"


siteList = {
            "mosquito" : [
                "https://www.mosquitosquad.com/fairfield-westchester-rockland-county/special-offers/",
                "?LocalContactFormSpecialOffers_ITM0_Message"
                ],
            "pulseM" : [
                "https://know.pulsem.me/thank-you-demo-request-0-0/?hs_preview=wFwNLGFg-32338808939",
                "&fbuy_ref_code"
                ],
            "pronto" :[
                "https://prontoheat.com/",
                "?schedule_an_appointment_message"
                ],
            "pulseM": [
                "https://pulsem.me/",
                "?input-15"
                ]
            }

@app.route('/')
def main():
    utmParams = "&utm_source=pulseM&utm_medium=referral&utm_campaign=code"
    url = siteList[request.args.get('site')][0]
    formID = siteList[request.args.get('site')][1]
    refCode = request.args.get('fbuy_ref_code')
    location = url  + formID + "=" + refCode + utmParams
    return redirect(location)


if __name__ == '__main__':
    app.debug = True
    app.run()
