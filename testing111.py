from bs4 import BeautifulSoup

html = '''<!DOCTYPE html>
<html>
<head itemprop="Article" itemscope itemtype="http://schema.org/Article">
    <meta charset="UTF-8">
    <meta data-n-head="true" name="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
    <meta name="theme-color" content="#de698c">
    <meta http="Cache-Control" content="no-transform">
    <meta name="format-detection" content="telephone=no">
    <meta name="applicable-device" content="pc">
    <link rel="apple-touch-icon-precomposed" href="//static.hdslb.com/mobile/img/512.png">
    <link rel="icon" type="image/vnd.microsoft.icon" href="//www.bilibili.com/favicon.ico">
    <link rel="apple-touch-icon" href="//www.bilibili.com/favicon.ico">
    <meta name="name" content="学习资料">
    <meta itemprop="title" name="title" content="学习资料">
    <meta itemprop="description" name="description" content="学习资料仅供自学自用（有的是自己买的，有的是在网上搜到的，如有侵权，告知我删）1.三笔讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1-MAJkymqt8darVd8QnrX6w 提取码:4kc82.三笔真题讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1LGz5uuXTNxdXj28pu11oIw 提取码:jxwj3.影视《爱你罗茜》复制这段内容后打开百度网盘App，操作">
    <meta itemprop="keywords" name="keywords" content="高中英语,提取码,APP,唐顿庄园,爱你罗茜,百度网盘,资格证考试,老友记,HTTPS,有的是,学习资料,素质三连,翻译,英语,影视,学习,教资,">
    <meta itemprop="author" name="author" content="小源来">
    <meta itemprop="url" content="https://www.bilibili.com/read/cv8250309/">
    <meta itemprop="image" content="https://i0.hdslb.com/bfs/article/banner/48d18349f5f84770cf48ae2391184fee93d72d00.png">
    <meta itemprop="uploadDate" content="2020-11-6 22:34:47">
    <meta itemprop="datePublished" content="2020-11-6 22:34:47">
    <meta data-n-head="true" data-hid="og:type" property="og:type" content="article">
    <meta data-n-head="true" data-hid="og:title" property="og:title" content="学习资料">
    <meta data-n-head="true" data-hid="og:image" property="og:image" content="https://i0.hdslb.com/bfs/article/banner/48d18349f5f84770cf48ae2391184fee93d72d00.png">
    <meta data-n-head="true" data-hid="og:url" property="og:url" content="http://www.bilibili.com/read/cv8250309/">
    <meta name="renderer" content="webkit">
    <meta name="spm_prefix" content="333.341">
    <link data-n-head="true" rel="icon" type="image/x-icon" href="//www.bilibili.com/favicon.ico">
    <link data-n-head="true" rel="apple-touch-icon-precomposed" type="image/x-icon" href="http://static.hdslb.com/mobile/img/512.png">
    <link rel="Canonical" href="https://www.bilibili.com/read/cv8250309/">
    <link rel="stylesheet" type="text/css" href="//static.hdslb.com/phoenix/dist/css/comment.min.css?v=20201123">
    <title>学习资料 - 哔哩哔哩</title>

    <script type="application/ld+json">
      {
        "@context": "http://schema.org/",
        "@type": "Article",
        "@id": "https://www.bilibili.com/read/cv8250309/",
        "appid": "1580859622074471",
        "title": "学习资料",
        "images": "https://i0.hdslb.com/bfs/article/banner/48d18349f5f84770cf48ae2391184fee93d72d00.png",
        "thumbnailUrl":"https://i0.hdslb.com/bfs/article/banner/48d18349f5f84770cf48ae2391184fee93d72d00.png",
        "description": "学习资料仅供自学自用（有的是自己买的，有的是在网上搜到的，如有侵权，告知我删）1.三笔讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1-MAJkymqt8darVd8QnrX6w 提取码:4kc82.三笔真题讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1LGz5uuXTNxdXj28pu11oIw 提取码:jxwj3.影视《爱你罗茜》复制这段内容后打开百度网盘App，操作",
        "pubDate": "2020-11-6 22:34:47"
      }
    </script>
    <script>
      window.original = {
        cvid: "8250309",
        author: {
          name: "小源来",
          mid: "381395879"
        },
        banner_url: "",
        reprint: "0",
        summary: "学习资料仅供自学自用（有的是自己买的，有的是在网上搜到的，如有侵权，告知我删）1.三笔讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1-MAJkymqt8darVd8QnrX6w 提取码:4kc82.三笔真题讲义复制这段内容后打开百度网盘App，操作更方便哦。 链接:https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;1LGz5uuXTNxdXj28pu11oIw 提取码:jxwj3.影视《爱你罗茜》复制这段内容后打开百度网盘App，操作",
        media: "",
        actId: "0",
        dispute: {
          dispute: "",
          dispute_url: ""
        },
        spoiler: "0"
      }
    </script>
<link href="//s1.hdslb.com/bfs/static/jinkela/article/pcDetail.b997b19311962e29a26f7704e08b2248a7efde50.css" rel="stylesheet"/></head>
<body>
<div id="biliMainHeader" class="report-wrap-module" style="height: 56px;"></div>
<div class="page-container">
    <div class="nav-tab-bar">
      
        <a href="//www.bilibili.com/read/home?from=articleDetail" target="_self" class="logo">
        </a>
        <a href="//www.bilibili.com/read/home?from=articleDetail" target="_self" class="tab-item" data-tab-id="0">
          <span>推荐</span>
        </a>
        
          
          <a href="//www.bilibili.com/read/douga?from=articleDetail" target="_self" class="tab-item " data-tab-id="2">
            <span>动画</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/game?from=articleDetail" target="_self" class="tab-item " data-tab-id="1">
            <span>游戏</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/cinephile?from=articleDetail" target="_self" class="tab-item " data-tab-id="28">
            <span>影视</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/life?from=articleDetail" target="_self" class="tab-item  on" data-tab-id="3">
            <span>生活</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/interest?from=articleDetail" target="_self" class="tab-item " data-tab-id="29">
            <span>兴趣</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/lightnovel?from=articleDetail" target="_self" class="tab-item " data-tab-id="16">
            <span>轻小说</span>
          </a>
          
        
          
          <a href="//www.bilibili.com/read/technology?from=articleDetail" target="_self" class="tab-item " data-tab-id="17">
            <span>科技</span>
          </a>
          
        

      
    </div>
    <div class="up-info-holder">
      <div class="fixed-box">
        <div class="up-info-block">
          <a class="up-face-holder " href="//space.bilibili.com/381395879" target="_blank">
            <img class="up-face-image" data-face-src="//i2.hdslb.com/bfs/face/6d0c45e240f591d82f1018f843b058161d981234.jpg" src="//static.hdslb.com/images/member/noface.gif">
            
            
            
            

          </a>
          <div class="up-info-right-block">
            <div class="row">
              <a class="up-name" href="//space.bilibili.com/381395879" target="_blank">小源来</a>
              <span class="level"></span>
              <div class="nameplate-holder">
                <i class="nameplate"></i>
              </div>
            </div>
            <div class="row-2">
              粉丝:
              <span class="fans-num"></span>
              <span class="view">阅读:</span>
              <span class="view-num"></span>
            </div>
          </div>
        </div>
        <div class="follow-btn-holder  ">
          <span class="follow-btn">关注</span>
        </div>
        <div class="up-article-list-block report-wrap-module hidden" id="readRecommendInfo">
          <div class="block-title">
            推荐文章
          </div>
          <ul class="article-list">
          </ul>
        </div>
        <div class="more">
          <div class="top-bar">
            <label>更多</label>
          </div>
          <a class="ac-link" href="//www.bilibili.com/read/apply/" target="_blank">
            <div class="link">
              <span class="icon">
              </span>
              <p class="title">成为创作者</p>
              <p class="info">申请成为专栏UP主</p>
            </div>
          </a>
          <a href="//www.bilibili.com/blackboard/help.html#专栏相关" target="_blank">
            <div class="help">
              <span class="icon">
              </span>
              <p class="title">专栏帮助</p>
              <p class="info">查看专栏使用说明</p>
            </div>
          </a>
        </div>
      </div>
    </div>
    <div class="right-side-bar">
      <div class="to-comment">
        <div class="comment-num-holder">
          <span class="comment-num"></span>
        </div>
      </div>
      <div class="to-top"></div>
    </div>
    <div class="head-container">
        
        
            <div class="bangumi-rating-container"></div>
        
        <div class="argue-flag hidden"></div>
        <div class="title-container">
            <h1 class="title">学习资料</h1>
            <div class="info">
                <a class="category-link" href="//www.bilibili.com/read/life#rid=15" target="_blank"><span>日常</span></a>
                <span class="create-time" data-ts="1604673317"></span>
                <div class="article-data"></div>
            </div>
        </div>

        
        <div style="display:none" class="author-container">
            <a class="author-face" href="//space.bilibili.com/381395879" target="_blank">
                <img data-face-src="//i2.hdslb.com/bfs/face/6d0c45e240f591d82f1018f843b058161d981234.jpg" src="//i2.hdslb.com/bfs/face/6d0c45e240f591d82f1018f843b058161d981234.jpg" class="author-face-img">
                
                
                
            </a>
            <a class="author-name" href="//space.bilibili.com/381395879" target="_blank">小源来</a>
          <div class="attention-btn slim-border">关注</div>
        </div>
    </div>

    <div class="article-holder"><p>学习资料仅供自学自用（有的是自己买的，有的是在网上搜到的，如有侵权，告知我删）</p><p><br/></p><p>1.三笔讲义</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1-MAJkymqt8darVd8QnrX6w 提取码:4kc8</p><p><br/></p><p>2.三笔真题讲义</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1LGz5uuXTNxdXj28pu11oIw 提取码:jxwj</p><p><br/></p><p>3.影视《爱你罗茜》</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1xPZo2YhdeI_avuMW6XAtQQ 提取码:gf98.</p><p><br/></p><p>4.影视《唐顿庄园》</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1S0Tkd0r9PaMMx36au_Hpiw 提取码:kwac</p><p><br/></p><p>5.影视《老友记》</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1pCTmYqaIHO3esOilSnHFcA 提取码:ebz3</p><p><br/></p><p>6.教师资格证考试/中学科一科二、高中英语</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/18B1Bk_TMIrB_USESgaSemQ 提取码:4f04</p><p><br/></p><p>7.欧陆字典词库包</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1MeCTp9tDnoiwqDL4QSYA3A 提取码:2ayf</p><p><br/></p><p>8.BBC英语音标教程</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1wBdpw9K7F1_ksvMIjbzojA 提取码:c9ow</p><p><br/></p><p>9.catti三笔</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1dYMgAxT60-jd6IjRIJl5Vg 提取码:8ne1</p><p><br/></p><p>10.catti三口</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1Jx0D1VJvdq63hXYTCVyJDQ 提取码:2l6l</p><p><br/></p><p>11.韩语教程</p><p>复制这段内容后打开百度网盘App，操作更方便哦。 链接:https://pan.baidu.com/s/1uF_GfzOzoFmLDUz-hVEGOg 提取码:a957</p><figure class="img-box" contenteditable="false"><img data-src="//i0.hdslb.com/bfs/article/02db465212d3c374a43c60fa2625cc1caeaab796.png" class="cut-off-6"/></figure><p>🉑素质三连三连三连一下👀</p></div>
    
    
    <p class="authority">本文禁止转载或摘编</p>
    
     
    <ul class="tag-container">
        
        <li data-tag-id="546" class="tag-item">
          <span class="tag-border">
            <span class="tag-border-inner"></span>
          </span>
          <span class="tag-content">翻译</span>
        </li>
        
        <li data-tag-id="8816" class="tag-item">
          <span class="tag-border">
            <span class="tag-border-inner"></span>
          </span>
          <span class="tag-content">英语</span>
        </li>
        
        <li data-tag-id="11323" class="tag-item">
          <span class="tag-border">
            <span class="tag-border-inner"></span>
          </span>
          <span class="tag-content">影视</span>
        </li>
        
        <li data-tag-id="13160" class="tag-item">
          <span class="tag-border">
            <span class="tag-border-inner"></span>
          </span>
          <span class="tag-content">学习</span>
        </li>
        
        <li data-tag-id="4143168" class="tag-item">
          <span class="tag-border">
            <span class="tag-border-inner"></span>
          </span>
          <span class="tag-content">教资</span>
        </li>
        
    </ul>
    
    <div class="article-action">
      <div class="ops">
        <span class="like-btn">
          <i class="icon-video-details_like"></i>
          <span>--</span>
        </span>
        <span class="coin-btn">
          <i class="icon-video-details_throw-coin"></i>
          <span>--</span>
        </span>
        <span class="fav-btn">
          <i class="icon-video-details_collection"></i>
          <span>--</span>
        </span>
        <span class="share-container share-btn">
          分享到：<span></span>
        </span>
      </div>
      <div class="more">
        <!-- <i class="icon-general_more-actions"></i> -->
        <div class="more-ops-list">
          <ul>
            <li value="0">投诉或建议</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="article-list-holder-block"></div>
    <div class="draft-holder-block">
    </div>
    <div class="b-head comment-title-block">
      <span class="b-head-t comment-results" style="display: inline;"></span>
      <span class="b-head-t">评论</span>
    </div>
    <div class="comment-holder"></div>

</div>
<div id="biliMainFooter" class="report-wrap-module"></div>
<script src="//static.hdslb.com/public/intersection-observer.js"></script>
<script src="//static.hdslb.com/public/timing.min.js"></script>
<script>window.performanceLog.setSource('article');</script>
<script src="//static.hdslb.com/js/jquery-3.3.1.min.js"></script>
<script>
  window.reportMsgObj = {}
  window.reportConfig = {
    sample : 1,
    errorTracker : false ,
    resourceTracker: false ,
    scrollTracker: false,
    msgObjects : 'reportMsgObj'
  }
</script>
<script type="text/javascript" charset="utf-8" src="//s1.hdslb.com/bfs/seed/jinkela/header-v2/header.js"></script>
<script type="text/javascript" src="//s1.hdslb.com/bfs/seed/jinkela/footer-v2/footer.js"></script>
<script src="//s1.hdslb.com/bfs/seed/jinkela/short/config/biliconfig.js"></script>
<script type="text/javascript" src="//static.hdslb.com/phoenix/dist/js/comment.min.js?v=20201123"></script>
<script src="//s1.hdslb.com/bfs/static/biliapp/biliapp.js"></script>
<!-- <script type="text/javascript" src="//s1.hdslb.com/bfs/seed/log/report/log-reporter.js" crossorigin></script> -->
<script>
  (function(){
  var src = (document.location.protocol == "http:") ? "http://js.passport.qihucdn.com/11.0.1.js?e6352779c080ceddc1bc4c6bbe047b69":"https://jspassport.ssl.qhimg.com/11.0.1.js?e6352779c080ceddc1bc4c6bbe047b69";
  document.write('<script src="' + src + '" id="sozz"><\/script>');
  })();
</script>
<script>
  window.addEventListener('beforeunload', function(){
    window.reportMsgObj['pageunload'] = document.hidden
  })
</script>
<script type="text/javascript" src="//s1.hdslb.com/bfs/static/jinkela/article/manifest.b997b19311962e29a26f7704e08b2248a7efde50.js"></script><script type="text/javascript" src="//s1.hdslb.com/bfs/static/jinkela/article/vendor.b997b19311962e29a26f7704e08b2248a7efde50.js"></script><script type="text/javascript" src="//s1.hdslb.com/bfs/static/jinkela/article/pcDetail.b997b19311962e29a26f7704e08b2248a7efde50.js"></script></body>
</html>
'''

b = BeautifulSoup(html,"html.parser")
print(type(b))
b.prettify()
print(type(b))
print(b)