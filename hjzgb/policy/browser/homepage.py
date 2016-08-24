#-*- coding: UTF-8 -*-
from Products.CMFPlone.resources import add_resource_on_request
from Products.Five.browser import BrowserView
from my315ok.products.product import Iproduct
from my315ok.products.productfolder import Iproductfolder
from plone.memoize.instance import memoize
from collective.diazotheme.bootstrap.browser.homepage import HomepageView as baseview
from hjzgb.policy.browser.interfaces import IThemeSpecific 

class FrontpageView(baseview):
    
    def __init__(self,context, request):
        # Each view instance receives context and request as construction parameters
        self.context = context
        self.request = request
        add_resource_on_request(self.request, 'hjzgb-homepage')            

    
    def carouselid(self):
        return "carouselid"
    
    def active(self,i):
        if i == 0:
            return "active"
        else:
            return ""
        
    @memoize
    def carouselresult(self,id=None):
        
        out = """
        <div id="carousel-generic" class="carousel slide">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-generic" data-slide-to="1"></li>
    <li data-target="#carousel-generic" data-slide-to="2"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner">
    <div class="item active">
      <img src="http://www.xtshzz.org/xinwenzhongxin/tupianxinwen/xiangtanshishekuaizuzhishoucibishuzhanglianxikuaiyishenglizhaokai/@@images/image/preview" alt="..."/>
      <div class="carousel-caption">
        <h3>大会召开</h3>
      </div>
    </div>
    <div class="item">
      <img src="http://www.xtshzz.org/xinwenzhongxin/tupianxinwen/xiangtanshishekuaizuzhishoucibishuzhanglianxikuaiyishenglizhaokai/@@images/image/preview" alt="..."/>
      <div class="carousel-caption">
        <h3>大会召开</h3>
      </div>
    </div>
    <div class="item">
      <img src="http://www.xtshzz.org/xinwenzhongxin/tupianxinwen/xiangtanshishekuaizuzhishoucibishuzhanglianxikuaiyishenglizhaokai/@@images/image/preview" alt="..."/>
      <div class="carousel-caption">
        <h3>大会召开</h3>
      </div>
    </div>    
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-generic" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="#carousel-generic" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>

</div>
        """ 
        

        if id ==None:
            braindata = self.catalog()({'object_provides':Iproduct.__identifier__, 
                                    'b_start':0,
                                    'b_size':3,
                             'sort_order': 'reverse',
                             'sort_on': 'created'})
        else:
            folder = self.catalog()({'object_provides':Iproductfolder.__identifier__,
                                    'id':id})
            if not bool(folder):
                braindata = self.catalog()({'object_provides':Iproduct.__identifier__, 
                                    'b_start':0,
                                    'b_size':3,
                             'sort_order': 'reverse',
                             'sort_on': 'created'})
            else:
                braindata = self.catalog()({'object_provides':Iproduct.__identifier__,
                                            'path':folder[0].getPath(),
                                            'b_start':0,
                                            'b_size':3,
                                            'sort_order': 'reverse',
                                            'sort_on': 'created'})         
        brainnum = len(braindata)
        if brainnum == 0:return out        

        outhtml = """<div id="%s" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
        """ % (self.carouselid())
        outhtml2 = '</ol><div class="carousel-inner">'
        for i in range(brainnum):            
            out = """<li data-target='%(carouselid)s' data-slide-to='%(indexnum)s' class='%(active)s'>
            </li>""" % dict(indexnum=str(i),
                    carouselid=''.join(['#',self.carouselid()]),
                    active=self.active(i))
                                               
            outhtml = ''.join([outhtml,out])   # quick concat string
            objurl = braindata[i].getURL()
            objtitle = braindata[i].Title
            outimg = """<div class="%(classes)s">
                        <img src="%(imgsrc)s" alt="%(imgtitle)s"/>
                          <div class="carousel-caption">
                            <h3>%(imgtitle)s</h3>
                              </div>
                                </div>""" % dict(classes=''.join(["item ", self.active(i)]),
                     imgsrc=''.join([objurl, "/@@images/image/preview"]),imgtitle=objtitle)
            outhtml2 = ''.join([outhtml2,outimg])   # quick concat string                    
#        outhtml = outhtml +'</ol><div class="carousel-inner">'
        result = ''.join([outhtml,outhtml2])   # quick concat string
        out = """
        </div><a class="left carousel-control" href="%(carouselid)s" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left"></span>
  </a>
  <a class="right carousel-control" href="%(carouselid)s" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right"></span>
  </a>
</div>""" % dict(carouselid = ''.join(["#", self.carouselid()]))
        return ''.join([result,out])
                
              
# roll zone
        
    def rollheader(self):
        return u"新闻"
    
    def rollmore(self):
        return "http://www.hjzgb.cn/news/"
    
# video player

    def swf_locid(self):
        "return swf locator's id "
        
        return "video"               
        
      
