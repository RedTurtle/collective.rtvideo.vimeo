# -*- coding: utf-8 -*-

from urlparse import urlparse
from zope.interface import implements
from redturtle.video.interfaces import IVideoEmbedCode
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

from redturtle.video.browser.videoembedcode import VideoEmbedCode

class VimeoEmbedCode(VideoEmbedCode):
    """ VimeoEmbedCode 
    provides a way to have a html code to embed Vimeo video in a web page 

    >>> from zope.interface import implements
    >>> from redturtle.video.interfaces import IRTRemoteVideo
    >>> from redturtle.video.interfaces import IVideoEmbedCode
    >>> from zope.component import getMultiAdapter
    >>> from redturtle.video.tests.base import TestRequest

    >>> class RemoteVideo(object):
    ...     implements(IRTRemoteVideo)
    ...     remoteUrl = 'http://vimeo.com/2075738'
    ...     size = {'width': 400, 'height': 225}
    ...     def getRemoteUrl(self):
    ...         return self.remoteUrl
    ...     def getWidth(self):
    ...         return self.size['width']
    ...     def getHeight(self):
    ...         return self.size['height']

    >>> remotevideo = RemoteVideo()
    >>> adapter = getMultiAdapter((remotevideo, TestRequest()), 
    ...                                         IVideoEmbedCode, 
    ...                                         name = 'vimeo.com')
    >>> adapter.getVideoLink()
    'https://player.vimeo.com/video/2075738'

    >>> print adapter()
    <div class="vimeoEmbedWrapper">
    <iframe width="400" height="225" frameborder="0"
            webkitallowfullscreen="webkitallowfullscreen"
            mozallowfullscreen="mozallowfullscreen"
            allowfullscreen="allowfullscreen"
            src="https://player.vimeo.com/video/2075738">
    </iframe>
    </div>
    <BLANKLINE>

    """
    template = ViewPageTemplateFile('vimeoembedcode_template.pt')

    def getVideoLink(self):
        video_id = urlparse(self.context.getRemoteUrl())[2][1:]
        return "https://player.vimeo.com/video/%s" % video_id
