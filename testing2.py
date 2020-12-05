import re
from methods import tools
import requests
import random

url = 'http://blog.sina.com.cn/s/blog_75f3efcb0102zdy5.html'

linkRe = re.compile(
    r'(https://pan.baidu.com/s/.{23}|https:&amp;#47;&amp;#47;pan.baidu.com&amp;#47;s&amp;#47;.{23}|https:&#47;&#47;pan.baidu.com&#47;s&#47;.{23}|https：pan.baidu.com s ).*?(提取码: .{4}|提取码：.{4}|提取码:.{4})')  # 回头加入完整的

user_agent = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
    'mozilla/5.0(macintosh;u;intelmacosx10_6_8;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(windows;u;windowsnt6.1;en-us)applewebkit/534.50(khtml,likegecko)version/5.1safari/534.50',
    'mozilla/5.0(macintosh;intelmacosx10.6;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'mozilla/5.0(windowsnt6.1;rv:2.0.1)gecko/20100101firefox/4.0.1',
    'opera/9.80(macintosh;intelmacosx10.6.8;u;en)presto/2.8.131version/11.11',
    'opera/9.80(windowsnt6.1;u;en)presto/2.8.131version/11.11',

]
header = {"User-Agent": random.choice(user_agent)}
r = requests.get(url, headers=header)
html = r.text
html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>音频试听：马勒第五交响曲多版本_长桥卧坡_新浪博客</title>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE8,chrome=1" />
<meta name="renderer" content="webkit">
<meta name="keywords" content="音频试听：马勒第五交响曲多版本_长桥卧坡_新浪博客,长桥卧坡," />
<meta name="description" content="音频试听：马勒第五交响曲多版本_长桥卧坡_新浪博客,长桥卧坡," />
<meta http-equiv="mobile-agent" content="format=html5; url=http://blog.sina.cn/dpool/blog/s/blog_75f3efcb0102zdy5.html?vt=4">
<meta http-equiv="mobile-agent" content="format=wml; url=http://blog.sina.cn/dpool/blog/ArtRead.php?nid=75f3efcb0102zdy5&vt=1">
<!–[if lte IE 6]>
<script type="text/javascript">
try{
document.execCommand("BackgroundImageCache", false, true);
}catch(e){}
</script>
<![endif]–>
<script type="text/javascript">
    
window.staticTime=new Date().getTime();
;(function () {
    if(/\/{2,}/.test(location.pathname)){
        location.href = 'http://blog.sina.com.cn' + location.pathname.replace(/\/+/g,'/') + location.search;
    }
})();
</script>
<link rel="pingback" href="http://upload.move.blog.sina.com.cn/blog_rebuild/blog/xmlrpc.php" />
<link rel="EditURI" type="application/rsd+xml" title="RSD" href="http://upload.move.blog.sina.com.cn/blog_rebuild/blog/xmlrpc.php?rsd" />
<link href="http://blog.sina.com.cn/blog_rebuild/blog/wlwmanifest.xml" type="application/wlwmanifest+xml" rel="wlwmanifest" />
<link rel="alternate" type="application/rss+xml" href="http://blog.sina.com.cn/rss/1978920907.xml" title="RSS" />
<link href="http://simg.sinajs.cn/blog7style/css/conf/blog/article.css" type="text/css" rel="stylesheet" /><link href="http://simg.sinajs.cn/blog7style/css/common/common.css" type="text/css" rel="stylesheet" /><link href="http://simg.sinajs.cn/blog7style/css/blog/blog.css" type="text/css" rel="stylesheet" /><link href="http://simg.sinajs.cn/blog7style/css/module/common/blog.css" type="text/css" rel="stylesheet" /><style id="tplstyle" type="text/css">@charset "utf-8";@import url("http://simg.sinajs.cn/blog7newtpl/css/32/32_3/t.css");
</style>
<style id="positionstyle"  type="text/css">
.sinabloghead .blogtoparea{ left:175px;top:61.0625px;}
.sinabloghead .blognav{ left:175px;top:137.890625px;}
</style>
<style id="bgtyle"  type="text/css">
</style>
<style id="headtyle"  type="text/css">
</style>
<style id="navtyle"  type="text/css">
</style>
<script type="text/javascript" src="http://d1.sina.com.cn/litong/zhitou/sspnew.js"></script></head>
<body>
<!--$sinatopbar-->
<div style="z-index:512;" class="nsinatopbar">
  <div style="position:absolute;left:0;top:0;" id="trayFlashConnetion"></div>
  <div class="ntopbar_main"> 
    <a id="login_bar_logo_link_350" href="http://blog.sina.com.cn" target="_blank"><img class="ntopbar_logo" src="http://simg.sinajs.cn/blog7style/images/common/topbar/topbar_logo.gif" width="100" alt="新浪博客"></a>
    <div class="ntopbar_floatL">
      <div class="ntopbar_search" id="traySearchBar"></div>
	  <div class="ntopbar_ad" id="loginBarActivity" style="display:none;"></div>
    </div>
    <div class="ntopbar_loading"><img src="http://simg.sinajs.cn/blog7style/images/common/loading.gif">加载中…</div>
  </div>
</div>
<!--$end sinatopbar-->

<div class="sinabloga" id="sinabloga">
	<div id="sinablogb" class="sinablogb">

	   
 <div id="sinablogHead" class="sinabloghead">
     <div style="display: none;" id="headflash" class="headflash"></div>
	   <div id="headarea" class="headarea">
      <div id="blogTitle" class="blogtoparea">
      <h1 id="blogname" class="blogtitle"><a href="http://blog.sina.com.cn/u/1978920907"><span id="blognamespan">加载中...</span></a></h1>
	  		
					<div id="bloglink" class="bloglink"><a href="http://blog.sina.com.cn/u/1978920907">http://blog.sina.com.cn/u/1978920907</a>  <a onclick="return false;" class="CP_a_fuc" href="#" id="SubscribeNewRss">[<cite>订阅</cite>]</a><a class="CP_a_fuc" href="javascript:void(scope.pa_add.add('1978920907'));">[<cite>手机订阅</cite>]</a></div>
      </div>
      <div class="blognav" id="blognav">
      			  <div id="blognavBg" class="blognavBg"></div> <div class="blognavInfo"> 
		<span><a   href="http://blog.sina.com.cn/u/1978920907">首页</a></span>
      <span><a class="on" href="http://blog.sina.com.cn/s/articlelist_1978920907_0_1.html">博文目录</a></span>
      <!--<span><a href="">图片</a></span>-->
      <span class="last"><a  href="http://blog.sina.com.cn/s/profile_1978920907.html">关于我</a></span></div>
      </div>      		      
             <div class="autoskin" id="auto_skin">
       </div>

<div class="adsarea">
     <a href="#"><div id="template_clone_pic" class="pic"></div></a>
     <div id="template_clone_link" class="link wdc_HInf"></div>
     <div id="template_clone_other" class="other"></div>        
</div>
    </div>
    </div>
    
    <!--主题内容开始 -->
    <div class="sinablogbody" id="sinablogbody">
		
	<!--第一列start-->
    <div id="column_1" class="SG_colW21 SG_colFirst"><div class="SG_conn" id="module_901">
    <div class="SG_connHead">
            <span class="title" comp_title="个人资料">个人资料</span>
            <span class="edit">
                        </span>
    </div>
    <div class="SG_connBody">
        <div class="info">
                         
            <div class="info_img" id="comp_901_head"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://portrait4.sinaimg.cn/1978920907/blog/180" id="comp_901_head_image" width="180" height="180" alt="长桥卧坡" title="长桥卧坡" /></div>
            
            <div class="info_txt">
              <div class="info_nm">
                <img id="comp_901_online_icon" style="display:none;" class="SG_icon SG_icon1" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="15" height="15" align="absmiddle" />
                <span class="SG_txtb"><strong id="ownernick">长桥卧坡                                </strong></span>
                
                <div class="clearit"></div>
              </div>
              <div class="info_btn1">
                <a target="_blank" href="http://weibo.com/u/1978920907?source=blog" class="SG_aBtn SG_aBtn_ico"><cite><img class="SG_icon SG_icon51" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="15" height="15" align="absmiddle" />微博</cite></a>
                <div class="clearit"></div>
              </div>
    <div class="SG_j_linedot"></div>        <div class="info_locate" id = "info_locate_id">
<div class="SG_j_linedot"></div>
<div class="info_btn2">
    <p>
    <a href="javascript:void(0);" class="SG_aBtn " id="comp901_btn_invite"><cite >加好友</cite></a>
    <a href="javascript:void(0);" class="SG_aBtn" id="comp901_btn_sendpaper"><cite >发纸条</cite></a>
    </p>
    <p>
    <a href="http://blog.sina.com.cn/s/profile_1978920907.html#write" class="SG_aBtn"   id="comp901_btn_msninfo"><cite>写留言</cite></a>
    <a href="#" onclick="return false;" class="SG_aBtn"  id="comp901_btn_follow"><cite onclick="Module.SeeState.add()">加关注</cite></a>
    </p>
    <div class="clearit"></div>
</div>
<div class="SG_j_linedot"></div>
</div>
                  <div class="info_list">     
                                   <ul class="info_list1">
                    <li><span class="SG_txtc">博客等级：</span><span id="comp_901_grade"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src="http://simg.sinajs.cn/blog7style/images/common/number/1.gif"  /><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src="http://simg.sinajs.cn/blog7style/images/common/number/5.gif"  /></span></li>
                    <li><span class="SG_txtc">博客积分：</span><span id="comp_901_score"><strong>0</strong></span></li>
                    </ul>
                    <ul class="info_list2">
                    <li><span class="SG_txtc">博客访问：</span><span id="comp_901_pv"><strong>71,556</strong></span></li>
                    <li><span class="SG_txtc">关注人气：</span><span id="comp_901_attention"><strong>38</strong></span></li>
                    <li><span class="SG_txtc">获赠金笔：</span><strong id="comp_901_d_goldpen">0支</strong></li>
                    <li><span class="SG_txtc">赠出金笔：</span><strong id="comp_901_r_goldpen">0支</strong></li>
					<li class="lisp" id="comp_901_badge"><span class="SG_txtc">荣誉徽章：</span></li>
                    </ul>
                  </div>
<div class="clearit"></div>
    </div>
    <div class="clearit"></div>
</div>
            </div>       
            <div class="SG_connFoot"></div>
</div>
<div id="module_903" class="SG_conn ">
    <div class="SG_connHead">
    <span comp_title="相关博文" class="title">相关博文</span>
    <span class="edit"> </span>
    </div>
    <div class="SG_connBody">
    <div class="atcTitList relaList">        <ul class="">

                <li class="SG_j_linedot1" style="display:none;">
            <p id="atcTitLi_SLOT_41" class="atcTitCell_tit SG_dot" style="display:none">
        </p>
        </li>
        <li class="SG_j_linedot1" style="display:none;">
            <p id="atcTitLi_SLOT_42"  class="atcTitCell_tit SG_dot" style="display:none">
        </p>
        </li>
        
                	</ul>
    <div class="atcTit_more"><span class="SG_more"><a href="http://blog.sina.com.cn/" target="_blank">更多&gt;&gt;</a></span></div></div>    </div>
    <div class="SG_connFoot"></div>
  </div>
<div id="module_904_top_ad"></div>
<div class="SG_conn " id="module_904">
<div class="SG_connHead">
<span class="title">推荐博文</span>
</div>
<div class="SG_connBody ">
	<div class="atcTitList relaList">		<ul class="">
					</ul>
		<div id="atcPicList">
		</div>
	<div class="atcTit_more"><span class="SG_more"><a target="_blank" href="http://blog.sina.com.cn/">查看更多</a>&gt;&gt;</span></div></div></div>
<div class="SG_connFoot"></div>
</div>
        <div class="SG_conn" id="module_47"><div class="SG_connHead">
                <span class="title" comp_title="谁看过这篇博文">谁看过这篇博文</span>
                                <span class="edit"></span>
            </div>
            <div class="SG_connBody">
            	<div class="wdtLoading"><img src="http://simg.sinajs.cn/blog7style/images/common/loading.gif" />加载中…</div>            </div>
            <div class="SG_connFoot"></div>
                  </div></div>
	<!--第一列end-->
	
	<!--第二列start-->
	<div id="column_2" class="SG_colW73">	
<div id="module_920" class="SG_conn">
	<div class="SG_connHead">
	    <span comp_title="正文" class="title">正文</span>
	    <span class="edit"><span id="articleFontManage" class="fontSize">字体大小：<a href="javascript:;" onclick="changeFontSize(2);return false;">大</a> <strong>中</strong> <a href="javascript:;" onclick="changeFontSize(0);return false;">小</a></span></span>
	</div>
    <div class="SG_connBody">
<!--博文正文 begin -->
	<div id="articlebody" class="artical" favMD5='{"75f3efcb0102zdy5":"80f0e0973eaa4a36d0ca0010b4ff955b"}'>
		<div class="articalTitle"> 
			
								<h2 id="t_75f3efcb0102zdy5" class="titName SG_txta">音频试听：马勒第五交响曲多版本</h2>
			
					<span class="img2">
				<img width="15" height="15" align="absmiddle" title="此博文包含图片" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" class="SG_icon SG_icon18"/>	
			</span>
					<span class="time SG_txtc">(2019-06-27 14:03:05)</span><div class="turnBoxzz"><a href="javascript:;" class="SG_aBtn SG_aBtn_ico SG_turn"  action-type="reblog" action-data="{srcBlog:1, blogId:'75f3efcb0102zdy5'}"><cite><img class="SG_icon SG_icon111" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="15" height="15" align="absmiddle">转载<em class="arrow">▼</em></cite></a></div>		</div>
		<div class="articalTag" id="sina_keyword_ad_area">
			<table>
				<tr>
					<td class="blog_tag">
					<script>
					var $tag='';
					var $tag_code='8d93de23195074b85f46fd83d4d92eed';
					var $r_quote_bligid='75f3efcb0102zdy5';
					var $worldcup='0';
					var $worldcupball='0';
					</script>
										</td>
					<td class="blog_class">
											<span class="SG_txtb">分类：</span>
						<a target="_blank" href="http://blog.sina.com.cn/s/articlelist_1978920907_4_1.html">唱片札记系列</a>
										</td>
				</tr>
			</table>
		</div>
						<!-- 正文开始 -->
		<div id="sina_keyword_ad_area2" class="articalContent   newfont_family">
			<a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYCKrpsZb1" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s2.sinaimg.cn/mw690/0029VlJ9zy7uYCKrpsZb1&amp;690" WIDTH="360" HEIGHT="349" NAME="image_operate_16551561615751772"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
<br />
西诺波利1985年DG版&amp;爱乐乐团（整轨）：<a HREF="" TARGET="_blank">https://pan.baidu.com/s/17ENHabT9xIWcLaM7toS_3w</A>&nbsp;<wbr>提取码：2eu2
<div><br />
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYCMjVSAc4" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s5.sinaimg.cn/mw690/0029VlJ9zy7uYCMjVSAc4&amp;690" WIDTH="360" HEIGHT="342" NAME="image_operate_29221561616318633"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A></DIV>
<div><br /></DIV>
<div>赞德2001TELARC版&amp;爱乐乐团（整轨）：<a HREF="" TARGET="_blank">https://pan.baidu.com/s/1HReuUaDT3kl5yEJj9B-PUw</A>&nbsp;<wbr>提取码：62it</DIV>
<div><br /></DIV>
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYDtaeaV7d" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s14.sinaimg.cn/mw690/0029VlJ9zy7uYDtaeaV7d&amp;690" WIDTH="360" HEIGHT="355" NAME="image_operate_85121561616336533"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
<br />
伯恩斯坦1963年SONY版&amp;纽约爱乐团：<a HREF="https://pan.baidu.com/s/1eBLHkd2ylF4czr9FyK9-qA" TARGET="_blank">https://pan.baidu.com/s/1eBLHkd2ylF4czr9FyK9-qA</A>&nbsp;<wbr>
提取码：235q</DIV>
</DIV>
<div><br /></DIV>
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYDuNNc125" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s6.sinaimg.cn/mw690/0029VlJ9zy7uYDuNNc125&amp;690" WIDTH="360" HEIGHT="351" NAME="image_operate_67131561616490861"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
<br /></DIV>
<div>伯恩斯坦1987DG版&amp;维也纳爱乐团：<a HREF="https://pan.baidu.com/s/1YtbmH676S693R3A8-893RA" TARGET="_blank">https://pan.baidu.com/s/1YtbmH676S693R3A8-893RA</A>&nbsp;<wbr>
提取码：8tit</DIV>
<div><br /></DIV>
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYDBrf6p61" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s2.sinaimg.cn/mw690/0029VlJ9zy7uYDBrf6p61&amp;690" WIDTH="400" HEIGHT="404" NAME="image_operate_47861561616798166"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
&nbsp;<wbr>滕斯泰特1978全集版&amp;伦敦爱乐团：</DIV>
<div>第1.2乐章：<a HREF="https://pan.baidu.com/s/1tlU6y_qefkH47L92N7P-1Q" TARGET="_blank">https://pan.baidu.com/s/1tlU6y_qefkH47L92N7P-1Q</A>&nbsp;<wbr>
提取码：vr31</DIV>
<div>第3.4.5乐章：<a HREF="https://pan.baidu.com/s/16W4H5XUlZxqV_ak6QwMHBg" TARGET="_blank">https://pan.baidu.com/s/16W4H5XUlZxqV_ak6QwMHBg</A>&nbsp;<wbr>
提取码：7ndy</DIV>
<div><br /></DIV>
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYDWW5me66" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s7.sinaimg.cn/mw690/0029VlJ9zy7uYDWW5me66&amp;690" WIDTH="360" HEIGHT="353" NAME="image_operate_11811561616937175"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
<br /></DIV>
<div>滕斯泰特1988EMI版&amp;伦敦爱乐团：<a HREF="https://pan.baidu.com/s/1rV-eaQeFD_Bs8IYuzR_9ag" TARGET="_blank">https://pan.baidu.com/s/1rV-eaQeFD_Bs8IYuzR_9ag</A>&nbsp;<wbr>
提取码：ivzy</DIV>
<div><br /></DIV>
<div><br /></DIV>
<div><a HREF="http://album.sina.com.cn/pic/0029VlJ9zy7uYEbTSZ99f" TARGET="_blank"><img src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" real_src ="http://s16.sinaimg.cn/mw690/0029VlJ9zy7uYEbTSZ99f&amp;690" WIDTH="360" HEIGHT="347" NAME="image_operate_29691561617112819"  ALT="音频试听：马勒第五交响曲多版本"  TITLE="音频试听：马勒第五交响曲多版本" /></A><br />
<br /></DIV>
<div>滕斯泰特1984年东京现场版&amp;伦敦爱乐团：<a HREF="https://pan.baidu.com/s/11B9J5zcXELr91fUFNvFnaA" TARGET="_blank">https://pan.baidu.com/s/11B9J5zcXELr91fUFNvFnaA</A>&nbsp;<wbr>
提取码：is1w</DIV>							
		</div>
						<!-- 正文结束 -->
		<div id='share' class="shareUp nor">
        	<div class="share SG_txtb clearfix">
			<span class="share-title">分享：</span> 
			<div class="bshare-custom" style="display:inline;margin-left:5px;">
			</div>
			</div>
            <div class="up">
	        	<div title="喜欢后让更多人看到" id="dbox_75f3efcb0102zdy5" class="upBox upBox_click" style="cursor: pointer;">
	            	<p ti_title="音频试听：马勒第五交响曲多版本" id="dbox2_75f3efcb0102zdy5" class="count" ></p>
	                <p class="link"><img width="15" height="15" align="absmiddle" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" class="SG_icon SG_icon34">喜欢</p>
	            </div>
<!--
                <div class="upBox upBox_add">
                    <p class="count">0</p>
                    <p class="link"><img width="20" height="16" align="absmiddle" title="推荐" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" class="SG_icon SG_icon214">赠金笔</p>
                </div>
-->
                                <div class="upBox upBox_add">
                    <p class="count" id="goldPan-num">0</p>
                    <p class="link" id="goldPan-give"><img class="SG_icon SG_icon214" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="20" height="16" title="赠金笔" align="absmiddle">赠金笔</p>
                </div>
                
	        </div>
            <div class="clearit"></div>
		</div>
		<div class="articalInfo">
			<!-- 分享到微博 {$t_blog} -->
			<div>
				阅读<span id="r_75f3efcb0102zdy5" class="SG_txtb"></span><em class="SG_txtb">┊</em> 
				<a href="#commonComment">评论</a> <span id="c_75f3efcb0102zdy5" class="SG_txtb"></span><em class="SG_txtb">┊</em>				<a href="javascript:;" onclick="$articleManage('75f3efcb0102zdy5',5);return false;">收藏</a><span id="f_75f3efcb0102zdy5"  class="SG_txtb"></span>
				<em class="SG_txtb">┊</em><a href="#" id="quote_set_sign" onclick="return false ;">转载</a><a  href="#" id="z_75f3efcb0102zdy5" onclick="return false ;" class="zznum"></a>				<span id="fn_音频试听：马勒第五交响曲多版本" class="SG_txtb"></span><em class="SG_txtb">┊</em>
				<a onclick="return false;" href="javascript:;" ><cite id="d1_digg_75f3efcb0102zdy5">喜欢</cite></a><a id="d1_digg_down_75f3efcb0102zdy5" href="javascript:;" ><b>▼</b></a>
									<em class="SG_txtb">┊</em><a href="http://blog.sina.com.cn/main_v5/ria/print.html?blog_id=blog_75f3efcb0102zdy5" target="_blank">打印</a><em class="SG_txtb">┊</em><a id="q_75f3efcb0102zdy5" onclick="report('75f3efcb0102zdy5');return false;" href="#">举报/Report</a>
											</div>
			<div class="IR">
				<table>
					<tr><!--
											<th class="SG_txtb" scope="row">已投稿到：</th>
						<td>
							<div class="IR_list">
								<span><img class="SG_icon SG_icon36" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="15" height="15" title="排行榜" align="absmiddle" /> <a href="http://blog.sina.com.cn/lm/114/117/day.html" class="SG_linkb" target="_blank">排行榜</a></span>							</div>
						</td>
					-->
					</tr>
									</table>
			</div>
		</div>
		<div class="clearit"></div>
		<div class="blogzz_zzlist borderc" id="blog_quote" style="display:none">加载中，请稍候......</div>
		<div class="articalfrontback SG_j_linedot1 clearfix" id="new_nextprev_75f3efcb0102zdy5">
							<div><span class="SG_txtb">前一篇：</span><a href="http://blog.sina.com.cn/s/blog_75f3efcb0102zdxa.html">马勒第五交响曲——多版本鉴赏</a></div>
										<div><span class="SG_txtb">后一篇：</span><a href="http://blog.sina.com.cn/s/blog_75f3efcb0102ze4v.html">最好听的亨德尔——马利纳马泽尔海丁克等</a></div>
					</div>
		<div class="clearit"></div>
							
		<div id="loginFollow"></div>
				<div class="allComm">
			<div  class="allCommTit" >
				<div class="SG_floatL">
				    <strong>评论</strong>
				    <span id="commAd_1" style="display:none;">
				        <span style="margin-left:15px; width:220px; display:inline-block;"><a target="_blank" href="http://blog.sina.com.cn/lm/8/2009/0325/105340.html">重要提示：警惕虚假中奖信息</a></span>
				    </span>
				</div>
				<div class="SG_floatR"><a class="CP_a_fuc" href="#post">[<cite>发评论</cite>]</a></div>
			</div>
			<ul id="article_comment_list" class="SG_cmp_revert"><!-- 循环始 --><li>评论加载中，请稍候...</li><!-- 循环终  --></ul>
			<div class="clearit"></div>
			<div class="myCommPages SG_j_linedot1">
				<div class="SG_page" id="commentPaging" style="display:none;">
					<ul class="SG_pages">
					</ul>
				</div>
				<div class="clearit"></div>
			</div>
			<a name="post"></a>
			<div class="writeComm">
				<div class="allCommTit">
					<div class="SG_floatL">
					    <strong>发评论</strong>
					    <span></span>
					</div>
					<div class="SG_floatR"></div>
				</div>
				<div class="wrCommTit">
					<div class="SG_floatL" id="commentNick" style="display:none;"></div>
				</div>
				<div class="formTextarea">
					<div style="float:left;" id="commonComment">
					<iframe id="postCommentIframe"  frameborder="0" style="border:1px solid #C7C7C7;
		height:158px;width:448px;maring-top:1px;background-color:white;" src="http://blog.sina.com.cn/main_v5/ria/blank2.html"></iframe>
					<textarea id="commentArea" tabindex="1" style="display:none;"></textarea>
					</div>
					<div id="mobileComment" style="float:left;display:none;">
						<textarea id="mbCommentTa" style="width:438px;height:150px;border:1px solid #C7C7C7;line-height:18px;padding:5px;"></textarea>
					</div>
					<div class="faceblk" id="faceWrap">
						<div id="smilesSortShow" class="faceline1">
						</div>
						<ul id="smilesRecommended" class="faceline01"></ul>
					</div>
					<div class="clearit"></div>
				</div>
				<div class="formLogin">
					<div class="SG_floatL"> 
					<p id="commentlogin" style="display:none;"><span>登录名：</span><input type="text" style="width: 115px;" id="login_name" tabindex="2"/>   <span>密码：</span><input type="password" style="width: 115px;" id="login_pass" tabindex="3"/>   <a href="https://login.sina.com.cn/getpass.html" target="_blank">找回密码</a>   <a href="https://login.sina.com.cn/signup/signup.php?entry=blog&src=blogicp&srcuid=1978920907" target="_blank">注册</a>	<input type="checkbox" id="login_remember"/><label for="login_remember" style="display:inline-block;" title="建议在网吧/公用电脑上取消该选项">记住登录状态</label></p><p id="commentloginM" style="display:none;"><span>昵&nbsp;&nbsp;&nbsp;称：</span><input type="text" style="width: 115px;" id="comment_anonyous"  value="新浪网友"/ tabindex="2" disabled></p><p id="quote_comment_p"><!--<input type="checkbox" id="bb"> <label for="bb"><img height="18" align="absmiddle" width="18" title="" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" class="SG_icon SG_icon110">分享到微博 <img height="15" align="absmiddle" width="15" title="新" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" class="SG_icon SG_icon11"></label>&nbsp;&nbsp;&nbsp;--><input type="checkbox" id="cbCommentQuote" /><label for="cbCommentQuote">评论并转载此博文</label><img class="SG_icon SG_icon11" src="http://simg.sinajs.cn/blog7style/images/common/sg_trans.gif" width="15" height="15" title="新" align="absmiddle" /></p>
					<p id="geetest-box" ></p>
					</div>

					<span style="display: none; color: rgb(153, 153, 153); margin-left: 10px;" id="login_remember_caution"></span>

											<!--<div class="SG_floatR" id="anonymity_cont"><input type="checkbox" id="anonymity"/><label for="anonymity">匿名评论</label></div>-->
									</div>
				<div class="formBtn">
					<a href="javascript:;" onclick="return false;" class="SG_aBtn" tabindex="5"><cite id="postcommentid">发评论</cite></a>
					<p class="SG_txtc">以上网友发言只代表其个人观点，不代表新浪网的观点或立场。</p>
				</div>
			</div>
		</div>
				<div class="clearit"></div>
		
				<div class="articalfrontback articalfrontback2 clearfix">
						  <div class="SG_floatL"><span class="SG_txtb">&lt;&nbsp;前一篇</span><a href="http://blog.sina.com.cn/s/blog_75f3efcb0102zdxa.html">马勒第五交响曲——多版本鉴赏</a></div>
									  <div class="SG_floatR"><span class="SG_txtb">后一篇&nbsp;&gt;</span><a href="http://blog.sina.com.cn/s/blog_75f3efcb0102ze4v.html">最好听的亨德尔——马利纳马泽尔海丁克等</a></div>
					</div>
		<div class="clearit"></div>
				
	</div>
	<!--博文正文 end -->
		<script type="text/javascript">
			var voteid="";
		</script>

            </div>       
            <div class="SG_connFoot"></div>
          </div>
</div>
	<!--第二列start-->
	
	<!--第三列start-->
	<div id="column_3" class="SG_colWnone"><div style="width:0px;height:0.1px;margin:0px;">&nbsp;&nbsp;</div></div>
	<!--第三列end-->

	
    </div>
   <!--主题内容结束 -->
  

	<div id="diggerFla" style="position:absolute;left:0px;top:0px;width:0px"></div>
    <div class="sinablogfooter" id="sinablogfooter"  style="position:relative;">
      
      <p class="SG_linka"><a href="http://help.sina.com.cn/" target="_blank">新浪BLOG意见反馈留言板</a>　电话：4000520066 提示音后按1键（按当地市话标准计费）　欢迎批评指正</p>
   
      <p class="SG_linka"><a href="http://corp.sina.com.cn/chn/" target="_blank">新浪简介</a> | <a href="http://corp.sina.com.cn/eng/" target="_blank">About Sina</a> | <a href="http://emarketing.sina.com.cn/" target="_blank">广告服务</a> | <a href="http://www.sina.com.cn/contactus.html" target="_blank">联系我们</a> | <a href="http://corp.sina.com.cn/chn/sina_job.html" target="_blank">招聘信息</a> | <a href="http://www.sina.com.cn/intro/lawfirm.shtml" target="_blank">网站律师</a> | <a href="http://english.sina.com" target="_blank">SINA English</a> | <a href="http://members.sina.com.cn/apply/" target="_blank">会员注册</a> | <a href="http://help.sina.com.cn/" target="_blank">产品答疑</a> </p>
      <p class="copyright SG_linka"> Copyright &copy; 1996 - 2018 SINA Corporation,  All Rights Reserved</p>
      <p class="SG_linka"> 新浪公司 <a href="http://www.sina.com.cn/intro/copyright.shtml" target="_blank">版权所有</a></p>
	  <a href="http://www.bj.cyberpolice.cn/index.jsp"  target="_blank" class="gab_link"></a>
    </div>
  </div>
</div>
<div id="swfbox"></div>
<script id="PVCOUNTER_FORIE" type="text/javascript"></script>
</body>
<script type="text/javascript">
var scope = {
    $newTray : 1,
    $setDomain : true,
    $uid : "1978920907",
    $PRODUCT_NAME : "blog7",      //blog7photo,blog7icp
    $pageid : "article",
    $key :  "1c32370d25e29a11e2646d29dbeda7ab",
    $uhost : "",
    $ownerWTtype :"",
    $private: {"pageset":0,"tj":0,"adver":0,"sms":0,"ad":0,"blogsize":0,"cms":0,"hidecms":0,"top":0,"invitationset":0,"p4p":0,"spamcms":1,"init7":1,"quote":0,"foot":0,"headpic":1,"isMsnLink":0,"msnfeed":"000","isMsnMove":0,"isprivate":0,"t_sina":"1978920907","oauth_token":1,"oauth_token_secret":1,"uname":"","p_push_t":1,"p_get_t":1,"articleclass":"117"},
    $summary: "...  (来自 @头条博客)",
    $is_photo_vip:0,
		 $nClass:0,
		 $articleid:"75f3efcb0102zdy5",
		 $sort_id:117,
		 $cate_id:"",
		 $isCommentAllow:0,
		 $album_pic:"0029VlJ9zy7uYCKrpsZb1",
		 $pn_x_rank:4,
		 $x_quote_c:"",
		 $flag2008:"",
		     component_lists:{"2":{"size":730,"list":[920]},"1":{"size":210,"list":[901,903,904,47]}},
    formatInfo:1,
    UserPic:[{"pid":"","repeat":"repeat-x","align-h":"center","align-v":"top","apply":"0"},{"pid":"","repeat":"repeat-x","align-h":"center","align-v":"top","apply":"0"},{"pid":"","repeat":"repeat-x","align-h":"center","align-v":"top","apply":"0"}],
    UserBabyPic:{"photoX":0,"photoY":0,"photoURL":null,"angle":0,"zoom":0,"maskX":0,"maskY":0,"maskURL":null,"frameURL":null},
    UserColor:1,
    backgroundcolor:"rgb(144, 218, 158)",
    $shareData:{"title":"\u97f3\u9891\u8bd5\u542c\uff1a\u9a6c\u52d2\u7b2c\u4e94\u4ea4\u54cd\u66f2\u591a\u7248\u672c@\u65b0\u6d6a\u535a\u5ba2","content":"  \u897f\u8bfa\u6ce2\u52291985\u5e74DG\u7248&\u7231\u4e50\u4e50\u56e2\uff08\u6574\u8f68\uff09\uff1ahttps:\/\/pan.baidu.com\/s\/17ENHabT9xIWcLaM7toS_3w  \u63d0\u53d6\u7801\uff1a2eu2     \u8d5e\u5fb72001TELARC...  (\u6765\u81ea @\u5934\u6761\u535a\u5ba2)","url":"http:\/\/blog.sina.com.cn\/s\/blog_75f3efcb0102zdy5.html","pic":"http:\/\/s2.sinaimg.cn\/middle\/0029VlJ9zy7uYCKrpsZb1&amp;690"},
    tpl:"32_3",
    reclist:0    };
var $encrypt_code = "fc24217588701c29a737181e4e705c2e";
</script>

<script type="text/javascript" src="http://sjs.sinajs.cn/blog7common/js/boot.js"></script>
<script type="text/javascript">__load_js();</script>
<script type="text/javascript">__render_page();</script>


<!--
<script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/buttonLite.js#style=-1&amp;uuid=b436f96b-ce3c-469f-93ca-9c0c406fcf10&amp;pophcol=2&amp;lang=zh"></script><script type="text/javascript" charset="utf-8" src="http://static.bshare.cn/b/bshareC0.js"></script>
<script type="text/javascript" charset="utf-8">
        bShare.addEntry({pic: "http://s2.sinaimg.cn/middle/0029VlJ9zy7uYCKrpsZb1&amp;690", title:"分享自长桥卧坡  《音频试听：马勒第五交响曲多版本》", summary:"...  (来自 @头条博客)"});
     </script>-->

<script type="text/javascript" src="http://sjs.sinajs.cn/xblogtheme/js/blog680-min.js"></script>
<script type="text/javascript">
        var slotArr = ['atcTitLi_SLOT_41', 'atcTitLi_SLOT_42','loginBarActivity']; //广告位id
        var sourceArr = ['SLOT_41','SLOT_42','SLOT_43,SLOT_47,SLOT_48'];  //广告资源id
        SinaBlog680.staticBox(slotArr, sourceArr);
</script>
</html>
'''
html = html.replace('\n', '')
# print(type(html))
for m in linkRe.finditer(html, re.S):
    if m:
        print(m.group(1), m.group(2))
