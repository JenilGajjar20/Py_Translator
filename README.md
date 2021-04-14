# Py_Translator

## tabulate
tabulate is a module that allows you to display table data beautifully. 
It is not a part of standard Python library, so tabulate needs to be installed: <b>pip install tabulate</b>

Module supports such tabular data types as:

<ul>
<li>list of lists (in general case - iterable of iterables)</li>
<li>dictionary list (or any other iterable object with dictionaries). Keys are used as column names</li>
<li>dictionary with iterable objects. Keys are used as column names</li>
</ul>

Function tabulate() is used to generate table: <Br>
<b> from tabulate import tabulate </b> <br>
<p> 
    data = [["Original Sentence:", "Translated Sentence:"],
                [self.word, str(translation.text)]]<br>
        return tabulate(data) 
</p>

### headers
Parameter headers allows you to pass an additional argument that specifies column names:  <br>
<p> 
    data = [["Original Sentence:", "Translated Sentence:"],
                [self.word, str(translation.text)]]<br>
    return tabulate(data, <b> headers="firstrow" </b>) 
</p>

### Table style
tabulate supports different table styles.
<p> 
    data = [["Original Sentence:", "Translated Sentence:"],
                [self.word, str(translation.text)]]<br>
    return tabulate(data, headers="firstrow",<b> tablefmt="fancy_grid" </b>)
</p>
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
