from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.template.loader import render_to_string
import datetime 
from django.shortcuts import render
import json
import requests
from django.http import HttpResponse
from django.utils.html import strip_tags                        
from datetime import datetime       
import googlemaps   
import smtplib
from googlemaps import convert
import cgpolyencode
import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape
from django.views.decorators.csrf import csrf_exempt 
from django.http import JsonResponse


from_email = ""
name = 'user'
to_email = ''
source_address = "5th Main Rd, Sector 6, HSR Layout, Bangalore, KA 560102"
destination_address = " 100 Feet Ring Road,Banashankari Stage III, Banashankari, Bengaluru, Karnataka 560085"                                                                                                               
    
def main(request):
    coords = drawmap()
    # coords['shipment_date'] = 
    # coords['start_time'] =
    coords['source_address'] = source_address 
    # coords['end_time'] = 
    coords['destination_address'] = destination_address
    # coords['vehicle_type'] =
    # coords['base_fee'] = 
    # coords['total_fee'] =
    # coords['vat'] =
    # coords['total_fee_with_vat'] = 
    coords['Username'] = name
    coords['to_email'] = to_email
    coords['shipping_fee'] = 2000
    coords['sender'] = "Fr3"
    url = "http://maps.googleapis.com/maps/api/staticmap?size=250x200&maptype=roadmap&format=jpg-baseline&extension=.jpeg&markers=color:red%7Clabel:A%7C"+str(coords['source_lat'])+","+str(coords['source_lng'])+"&markers=color:blue%7Clabel:B%7C"+str(coords['dstn_lat'])+","+str(coords['dstn_lng'])+"&path=weight:3%7Ccolor:blue%7Cenc:"+coords['a']
    #print url
    shortened_url = shortener(url)
    print shortened_url
    coords['url'] = shortened_url
    send_mail(coords)
    return render (request,'b.html',coords)

def shortener(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={{key}}'
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(post_url, data=json.dumps(payload), headers=headers)
    return eval(r.content)['id']
def get_coords(gmaps):
    #get coords from server
    # return list of coordinates

    coord_list = []
    #wen server is running uncomment
    # GEOTRACKING_URL = "http://192.168.1.34:8014/api/trip/SHP10270121887431792816"
    # try:
    #         resp = requests.get(GEOTRACKING_URL,
    #             verify=True) # NOTE(cbro): verify SSL certs.
            
    #         data = resp.json()['message']['data']
    #         shipment_id = resp.json()['message']['trip_id'] 

    #         for i in data:
    #             (lat,lng) = (float(i['lat']),float(i['long']))
    #             address = gmaps.reverse_geocode((lat,lng))
    #             address = (address[0]['geometry']['location'])
    #             coord_list.append(address)
                
    
    # except requests.exceptions.Timeout:
    #         raise requests.exceptions.Timeout()

    # if len(coord_list) >8:
    #     jump = len(coord_list)/8
    #     temp = []

    #     for i in range(8):
    #         temp.append(coord_list[i+jump])
    #     coord_list = temp


    # return (coord_list,shipment_id)


    resp = {"status":"success","message":{"trip_id":"SHP10270121887431792816","driver_id":"3","data":[{"lat":"12.9667","long":"77.5667","speed":"45.32"},{"lat":"13.054061","long":"77.476616","speed":"97"},{"lat":"13.054461","long":"77.477416","speed":"91"},{"lat":"13.054861","long":"77.478216","speed":"60"},{"lat":"13.055261","long":"77.479016","speed":"20"},{"lat":"13.055661","long":"77.479816","speed":"26"},{"lat":"13.056061","long":"77.480616","speed":"91"},{"lat":"13.056461","long":"77.481416","speed":"3"},{"lat":"13.056861","long":"77.482216","speed":"66"},{"lat":"13.057261","long":"77.483016","speed":"64"},{"lat":"13.057661","long":"77.483816","speed":"78"},{"lat":"13.058061","long":"77.484616","speed":"9"},{"lat":"13.058461","long":"77.485416","speed":"77"},{"lat":"13.058861","long":"77.486216","speed":"7"},{"lat":"13.059261","long":"77.487016","speed":"91"},{"lat":"13.059661","long":"77.487816","speed":"85"},{"lat":"13.060061","long":"77.488616","speed":"46"},{"lat":"13.060461","long":"77.489416","speed":"95"},{"lat":"13.060861","long":"77.490216","speed":"64"},{"lat":"13.061261","long":"77.491016","speed":"7"},{"lat":"13.061661","long":"77.491816","speed":"78"},{"lat":"13.062061","long":"77.492616","speed":"9"},{"lat":"13.062461","long":"77.493416","speed":"89"},{"lat":"13.062861","long":"77.494216","speed":"80"},{"lat":"13.063261","long":"77.495016","speed":"90"},{"lat":"13.063661","long":"77.495816","speed":"66"},{"lat":"13.064061","long":"77.496616","speed":"37"},{"lat":"13.064461","long":"77.497416","speed":"74"},{"lat":"13.064861","long":"77.498216","speed":"40"},{"lat":"13.065261","long":"77.499016","speed":"56"},{"lat":"13.065661","long":"77.499816","speed":"2"},{"lat":"13.066061","long":"77.500616","speed":"48"},{"lat":"13.066461","long":"77.501416","speed":"33"},{"lat":"13.066861","long":"77.502216","speed":"42"},{"lat":"13.067261","long":"77.503016","speed":"39"},{"lat":"13.067661","long":"77.503816","speed":"82"},{"lat":"13.068061","long":"77.504616","speed":"90"},{"lat":"13.068461","long":"77.505416","speed":"27"},{"lat":"13.068861","long":"77.506216","speed":"93"},{"lat":"13.069261","long":"77.507016","speed":"55"},{"lat":"13.069661","long":"77.507816","speed":"35"},{"lat":"13.070061","long":"77.508616","speed":"86"},{"lat":"13.070461","long":"77.509416","speed":"61"},{"lat":"13.070861","long":"77.510216","speed":"95"},{"lat":"13.071261","long":"77.511016","speed":"4"},{"lat":"13.071661","long":"77.511816","speed":"32"},{"lat":"13.072061","long":"77.512616","speed":"93"},{"lat":"13.072461","long":"77.513416","speed":"90"},{"lat":"13.072861","long":"77.514216","speed":"17"},{"lat":"13.073261","long":"77.515016","speed":"37"},{"lat":"13.073661","long":"77.515816","speed":"75"},{"lat":"13.074061","long":"77.516616","speed":"60"},{"lat":"13.074461","long":"77.517416","speed":"14"},{"lat":"13.074861","long":"77.518216","speed":"72"},{"lat":"13.075261","long":"77.519016","speed":"52"},{"lat":"13.075661","long":"77.519816","speed":"29"},{"lat":"13.076061","long":"77.520616","speed":"51"},{"lat":"13.076461","long":"77.521416","speed":"98"},{"lat":"13.076861","long":"77.522216","speed":"28"},{"lat":"13.077261","long":"77.523016","speed":"60"},{"lat":"13.077661","long":"77.523816","speed":"23"},{"lat":"13.078061","long":"77.524616","speed":"44"},{"lat":"13.078461","long":"77.525416","speed":"57"},{"lat":"13.078861","long":"77.526216","speed":"90"},{"lat":"13.079261","long":"77.527016","speed":"32"},{"lat":"13.079661","long":"77.527816","speed":"33"},{"lat":"13.080061","long":"77.528616","speed":"81"},{"lat":"13.080461","long":"77.529416","speed":"81"},{"lat":"13.080861","long":"77.530216","speed":"5"},{"lat":"13.081261","long":"77.531016","speed":"95"},{"lat":"13.081661","long":"77.531816","speed":"36"},{"lat":"13.082061","long":"77.532616","speed":"94"},{"lat":"13.082461","long":"77.533416","speed":"7"},{"lat":"13.082861","long":"77.534216","speed":"83"},{"lat":"13.083261","long":"77.535016","speed":"3"},{"lat":"13.083661","long":"77.535816","speed":"43"},{"lat":"13.084061","long":"77.536616","speed":"44"},{"lat":"13.084461","long":"77.537416","speed":"89"},{"lat":"13.084861","long":"77.538216","speed":"28"},{"lat":"13.085261","long":"77.539016","speed":"87"},{"lat":"13.085661","long":"77.539816","speed":"9"},{"lat":"13.086061","long":"77.540616","speed":"5"},{"lat":"13.086461","long":"77.541416","speed":"36"},{"lat":"13.086861","long":"77.542216","speed":"10"},{"lat":"13.087261","long":"77.543016","speed":"66"},{"lat":"13.087661","long":"77.543816","speed":"74"},{"lat":"13.088061","long":"77.544616","speed":"57"},{"lat":"13.088461","long":"77.545416","speed":"89"},{"lat":"13.088861","long":"77.546216","speed":"57"},{"lat":"13.089261","long":"77.547016","speed":"42"},{"lat":"13.089661","long":"77.547816","speed":"71"},{"lat":"13.090061","long":"77.548616","speed":"56"},{"lat":"13.090461","long":"77.549416","speed":"32"},{"lat":"13.090861","long":"77.550216","speed":"31"},{"lat":"13.091261","long":"77.551016","speed":"36"},{"lat":"13.091661","long":"77.551816","speed":"22"},{"lat":"13.092061","long":"77.552616","speed":"80"},{"lat":"13.092461","long":"77.553416","speed":"87"},{"lat":"13.092861","long":"77.554216","speed":"51"},{"lat":"13.093261","long":"77.555016","speed":"40"},{"lat":"13.093661","long":"77.555816","speed":"71"}]}}
    #resp = {"status":"success","message":{"trip_id":"SHP10270121887431792816","driver_id":"3","data":[{"lat":"12.9667","long":"77.5667","speed":"45.32"},{"lat":"13.054461","long":"77.477416","speed":"91"},{"lat":"13.054061","long":"77.476616","speed":"97"}]}}
    #print (float(data['message']['data'][0]['lat'])),(float(data['message']['data'][0]['long']))
    
    data = resp['message']['data']
    shipment_id = resp['message']['trip_id']


    for i in data:
        (lat,lng) = (float(i['lat']),float(i['long']))
        # address = gmaps.reverse_geocode((lat,lng))
        # address = (address[0]['geometry']['location'])

        address = {"lat":float(i['lat']), "lng":float(i['long'])}
        coord_list.append(address)


    if len(coord_list) >8:
        jump = len(coord_list)/8
        temp = []

        for i in range(8):
            temp.append(coord_list[i+jump])
        coord_list = temp


    return (coord_list,shipment_id)



    
    

def drawmap():
    
    gmaps = googlemaps.Client(key='key')
    #print 'ads'
    shipment_details = get_coords(gmaps)
    driver_route = shipment_details[0]
    #print driver_route
    shipment_id = shipment_details[1]
    # address= gmaps.reverse_geocode((12.934751400000000000, 77.612259199999930000))
    # address1 = gmaps.reverse_geocode((13.134958600000000000,77.589096700000030000))
    
    source_lat = 12.9667
    source_lng = 77.5667
    dstn_lat = 13.093661 
    dstn_lng = 77.555816


    directions_result = gmaps.directions((source_lat,source_lng),
                                     (dstn_lat,dstn_lng), waypoints = driver_route,   
                                     mode="driving",  
                                     departure_time=datetime.now())

    a = directions_result[0]['overview_polyline']['points']
    #print a

    # lst =  gmaps.geocode(source_address)[0]
    # geometry = lst['geometry']
    # #print geometry['location']['lat']
    

    return {'shipment_id':shipment_id, 'a':a,'source_lat':source_lat,'source_lng':source_lng,'dstn_lat':dstn_lat,'dstn_lng':dstn_lng}

    #send_mail(name,to_email,directions_result)
    
    # reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
    # #print reverse_geocode_result
def send_mail(coords):
    text_content = 'Welcome to shippr.in'
    html_content = get_template('b.html')
    html_content = html_content.render(Context(coords))
    subject = "Invoice Copy and Delivery Confirmation for Shippr.in"
    msg = EmailMultiAlternatives(
        subject, text_content, from_email, [to_email])
    msg.attach_alternative(html_content, "text/html")
    
    result = myview()


    msg.attach('invoicex.pdf', result[0].getvalue() , 'application/pdf')

    msg.send()

    


def _convert_waypoint(waypoint):
    if not convert.is_string(waypoint):
        return convert.latlng(waypoint)

    return waypoint
# '''Provides utility functions for encoding and decoding linestrings using the 
# Google encoded polyline algorithm.
# '''
 
# def encode_coords(coords):
#     '''Encodes a polyline using Google's polyline algorithm
    
#     See http://code.google.com/apis/maps/documentation/polylinealgorithm.html 
#     for more information.
    
#     :param coords: Coordinates to transform (list of tuples in order: latitude, 
#     longitude).
#     :type coords: list
#     :returns: Google-encoded polyline string.
#     :rtype: string    
#     '''
    
#     result = []
    
#     prev_lat = 0
#     prev_lng = 0
    
#     for x, y in coords:        
#         lat, lng = int(y * 1e5), int(x * 1e5)
        
#         d_lat = _encode_value(lat - prev_lat)
#         d_lng = _encode_value(lng - prev_lng)        
        
#         prev_lat, prev_lng = lat, lng
        
#         result.append(d_lat)
#         result.append(d_lng)
    
#     return ''.join(c for r in result for c in r)
    
# def _split_into_chunks(value):
#     while value >= 32: #2^5, while there are at least 5 bits
        
#         # first & with 2^5-1, zeros out all the bits other than the first five
#         # then OR with 0x20 if another bit chunk follows
#         yield (value & 31) | 0x20 
#         value >>= 5
#     yield value
 
# def _encode_value(value):
#     # Step 2 & 4
#     value = ~(value << 1) if value < 0 else (value << 1)
    
#     # Step 5 - 8
#     chunks = _split_into_chunks(value)
    
#     # Step 9-10
#     return (chr(chunk + 63) for chunk in chunks)





def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename="invoicex.pdf"'
        # email.attach('invoicex.pdf', result.getvalue() , 'application/pdf')
        # email.send()
        # return HttpResponse(result.getvalue(), content_type='application/pdf')
        return [result,response]

def myview():
    
    #Retrieve data or whatever you need
    

    return render_to_pdf(
            'Invoice_Bill.html',
            {
                'pagesize':'A4',
                'Cost':24,
                'items':[{"number":1000,"name":"sofa","cost":5000},{'number':2000,"name":"table","cost":5000}]
                
            }
        )

