import webapp2
from PIL import Image, ImageDraw
import StringIO
import urllib2
class Imagery(webapp2.RequestHandler):
  def get(self):
      url = 'http://graph.facebook.com/'+ self.request.get('id') + '/picture?type=large'
      self.response.headers['Content-Type'] = 'image/jpeg'
      self.response.write(self.asciii(url))
  def asciii(self,url):
      output = StringIO.StringIO()
      picturefromurl = StringIO.StringIO()
      chars = [' ','.', '`', '-', '~', '|', '^', '+', '>', '?', 'v', '}', 'r', 'w', 'z', 'x', 'u', 'y', 'K', 'k', 'p', 'q', 'H']
      picture = StringIO.StringIO(urllib2.urlopen(url).read())
      im = Image.open(picture)
      pixels = (im.size[0],im.size[1]*6/11)
      im = im.convert('L').resize(pixels).load()
      ascii = ''
      for i in xrange(pixels[1]):
          for j in xrange(pixels[0]):
              x = 256 - im[j,i]
              if x<253:
                  ascii += chars[x/11]
              else:
                  ascii += chars[22]
          ascii += '\n'
      ascii += 'Chlamydomonas Labs'
      im = Image.new('L', (6*pixels[0], 11*(pixels[1]+1)),255)
      lines = ascii.split('\n')
      for i in xrange(pixels[1]+1):
          imd = ImageDraw.Draw(im)
          imd.text((0,i*11),lines[i])
      im.save(output, format = "JPEG")
      contents = output.getvalue()
      return contents

class Download(webapp2.RequestHandler):
  def get(self):
      url = 'http://graph.facebook.com/'+ self.request.get('id') + '/picture?type=large'
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write(self.asciii(url))
  def asciii(self,url):
      picturefromurl = StringIO.StringIO()
      chars = [' ','.', '`', '-', '~', '|', '^', '+', '>', '?', 'v', '}', 'r', 'w', 'z', 'x', 'u', 'y', 'K', 'k', 'p', 'q', 'H']
      picture = StringIO.StringIO(urllib2.urlopen(url).read())
      im = Image.open(picture)
      pixels = (im.size[0],im.size[1]*6/11)
      im = im.convert('L').resize(pixels).load()
      ascii = ''
      for i in xrange(pixels[1]):
          for j in xrange(pixels[0]):
              x = 256 - im[j,i]
              if x<253:
                  ascii += chars[x/11]
              else:
                  ascii += chars[22]
          ascii += '\n'
      ascii += 'Chlamydomonas Labs'
      ascii += '\nGet Image version @ http://ascii-art-007.appspot.com/Imgfromurl?url='+ url
      return ascii
class Imagefromurl(webapp2.RequestHandler):
  def get(self):
      url = self.request.get('url')
      self.response.headers['Content-Type'] = 'image/jpeg'
      self.response.write(self.asciii(url))
  def asciii(self,url):
      output = StringIO.StringIO()
      picturefromurl = StringIO.StringIO()
      chars = [' ','.', '`', '-', '~', '|', '^', '+', '>', '?', 'v', '}', 'r', 'w', 'z', 'x', 'u', 'y', 'K', 'k', 'p', 'q', 'H']
      picture = StringIO.StringIO(urllib2.urlopen(url).read())
      im = Image.open(picture)
      pixels = (im.size[0],im.size[1]*6/11)
      im = im.convert('L').resize(pixels).load()
      ascii = ''
      for i in xrange(pixels[1]):
          for j in xrange(pixels[0]):
              x = 256 - im[j,i]
              if x<253:
                  ascii += chars[x/11]
              else:
                  ascii += chars[22]
          ascii += '\n'
      ascii += 'Chlamydomonas Labs'
      im = Image.new('L', (6*pixels[0], 11*(pixels[1]+1)),255)
      lines = ascii.split('\n')
      for i in xrange(pixels[1]+1):
          imd = ImageDraw.Draw(im)
          imd.text((0,i*11),lines[i])
      im.save(output, format = "JPEG")
      contents = output.getvalue()
      return contents
class Downloadfromurl(webapp2.RequestHandler):
  def get(self):
      url = self.request.get('url')
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.write(self.asciii(url))
  def asciii(self,url):
      picturefromurl = StringIO.StringIO()
      chars = [' ','.', '`', '-', '~', '|', '^', '+', '>', '?', 'v', '}', 'r', 'w', 'z', 'x', 'u', 'y', 'K', 'k', 'p', 'q', 'H']
      picture = StringIO.StringIO(urllib2.urlopen(url).read())
      im = Image.open(picture)
      pixels = (im.size[0],im.size[1]*6/11)
      im = im.convert('L').resize(pixels).load()
      ascii = ''
      for i in xrange(pixels[1]):
          for j in xrange(pixels[0]):
              x = 256 - im[j,i]
              if x<253:
                  ascii += chars[x/11]
              else:
                  ascii += chars[22]
          ascii += '\n'
      ascii += 'Chlamydomonas Labs'
      ascii += '\nGet Image version @ http://ascii-art-007.appspot.com/Imgfromurl?url='+ url
      return ascii

app = webapp2.WSGIApplication([('/Img', Imagery),('/Download', Download),('/Imgfromurl',Imagefromurl),('/Downloadfromurl',Downloadfromurl)],
                              debug=True)
