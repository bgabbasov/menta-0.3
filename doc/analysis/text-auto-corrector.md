# Text auto correct
Should check and correct text

There is no complite solution which can automatically check and correct spelling. all availlable libs can only give you a list of suitable corrections.

Tests were made in Libre office which uses Aspell and in Abiword which uses Enchant library


Results:

<Table>
<tr><td></td> <td>Libre Office</td> <td>Abiword </td> </tr>
<tr><td> found errors </td> <td> 8</td> <td> 5</td> </tr>
<tr> <td> not found errors</td> <td> 2</td> <td> 7</td> </tr>
<tr> <td>mistackes </td><td>10 </td> <td> 8</td> </tr>
<tr> <td> relevance of the proposed changes</td> <td> 30% </td> <td>70% </td> </tr>
</table>


you can add own dictionaries in both products.



I did test Kword because of many bugs, and OpenCog because it uses only Link Grammar which includeded in Abi word and can't get better rusults than AbiWord



# Suggested libraries
1. Jazzy http://jazzy.sourceforge.net/
1. link-grammar http://wiki.opencog.org/w/Natural_Language_Processing
