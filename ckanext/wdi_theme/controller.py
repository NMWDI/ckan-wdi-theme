import ckan.plugins as p
from ckan.lib.base import BaseController
from ckan.common import _, c, request, response
# import ckan.lib.mailer as mailer
import smtplib
from email.mime.text import MIMEText
# from email.message import EmailMessage
import logging

logger = logging.getLogger(__name__)


class WDIController(BaseController):
    def map(self):
        return p.toolkit.render('map.html')
    def team(self):
        return p.toolkit.render('team.html')
    def news(self):
        return p.toolkit.render('news.html')
    def faq(self):
        return p.toolkit.render('faq.html')
    def contact(self):
        return p.toolkit.render('contact.html')
    def reports(self):
        return p.toolkit.render('reports.html')
    def photos(self):
        return p.toolkit.render('photos.html')
    def events(self):
        return p.toolkit.render('events.html')  
    def contactmail(self):
        first=request.params.get('first', 'NOFIRSTNAME')
        last=request.params.get('last', 'NOLASTNAME')
        email=request.params.get('email', '')
        body=request.params.get('message', '')
        if len(email)==0 or len(body)==0:
            return p.toolkit.render('emailerror.html')
        sender = email
        recipients = ['Stacy Timmons <stacy.timmons@nmt.edu> ','Jeri Graham <jeri.graham@nmt.edu>']
        msg = MIMEText(body)
        msg['Subject'] = "Message from newmexicowaterdata.org contact form"
        msg['From'] = first+' '+last+' <'+sender+'>'
        msg['To'] = ", ".join(recipients)

        try:
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, recipients, msg.as_string())     
            logger.debug("Successfully sent email")
        except SMTPException as e:
            logger.debug(e)
            return p.toolkit.render('emailerror.html')

        return p.toolkit.render('emailgood.html')               
