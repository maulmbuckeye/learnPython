import unittest
from clean_bg import *

class testing (unittest.TestCase) : 
    sample_html = '<span id="en-ESV-15497" class="text Ps-98-6"><sup class="versenum">6&nbsp;</sup>With <sup class="crossreference" data-link="(<a href=&quot;#cen-ESV-15497N&quot; title=&quot;See cross-reference N&quot;>N</a>)" data-cr="#cen-ESV-15497N"></sup>trumpets and the sound of <sup class="crossreference" data-link="(<a href=&quot;#cen-ESV-15497O&quot; title=&quot;See cross-reference O&quot;>O</a>)" data-cr="#cen-ESV-15497O"></sup>the horn</span>'
    
    def test_small_caps_become_all_caps (self) :
        html = '<span class="small-caps">Lord</span> and <span class="small-caps">Lord</span>'
        result = clean_bg(html)
        self.assertEqual(str(result),"LORD and LORD")

    def test_remove_verse_numbers (self) :        
        html = '<sup class="versenum">6&nbsp;</sup>The'
        result = clean_bg(html)
        self.assertEqual(str(result),"The")
        
    def test_remove_crossreferences (self) :
        html = 'With <sup class="crossreference" data-link="(<a href=&quot;#cen-ESV-15497N&quot; title=&quot;See cross-reference N&quot;>N</a>)" data-cr="#cen-ESV-15497N"></sup>trumpets and the sound of <sup class="crossreference" data-link="(<a href=&quot;#cen-ESV-15497O&quot; title=&quot;See cross-reference O&quot;>O</a>)" data-cr="#cen-ESV-15497O"></sup>the horn'
        result = clean_bg(html)
        self.assertEqual(str(result),"With trumpets and the sound of the horn")
        
    def test_remove_indent_breaks(self) :
        html = 'Mi<span class="indent-1-breaks">&nbsp;&nbsp;&nbsp;&nbsp;</span>ke'
        result = clean_bg(html)
        self.assertEqual(str(result),"Mike")
     
    def test_get_verse_address (self) :
        html = '<span id="en-ESV-15497" class="text Ps-98-6">With trumpets and the sound of the horn</span>'
        self.assertEqual( get_verse_address(html), ("Ps","98","6"))
    
    def test_get_initial_verse(self) :
         html = '<span class="text">initial</span><span class="text">second</span>'
         for verse, desired_text in zip(verses(html),["initial","second"]) :
            self.assertEqual(verse.text, desired_text)
                     
    def test_remove_indent(self) :
        html = '<span class="indent-1">keep this</span>'
        result = clean_bg(html)
        self.assertEqual(str(result),"keep this")
        
    def test_remove_indent_with_subitems(self) :
        html = '<span class="indent-1"><span>inner</span>outter</span>'
        result = clean_bg(html)
        self.assertEqual(str(result),"<span>inner</span>outter")
    
    @unittest.skip("Need to really think about how to handle this")
    def test_multiple_span_verse(self) :
        html = '''
            <span class="text Ps-98-1">Sing</span>
            <span class="text Ps-98-1">to the Lord</span>
            <span class="text Ps-98-2">a new song</span>
            '''
        for verse, desired_text in zip(verses(html),["Sing to the Lord","a new song"]) :
            self.assertEqual(verse.text, desired_text)


        
        
if __name__ == "__main__" :
    unittest.main()