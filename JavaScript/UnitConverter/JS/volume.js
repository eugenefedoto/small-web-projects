/* volume.js - Convert Volumes
 */

"use strict";

/* Load the Factors from the JSON file.
 */
var conversionsV;
function saveReturn(data)
{
    conversionsV = JSON.parse(data);
}
ajaxFetch("./JS/volume.json", saveReturn);


function makeBoxesVolume()
{
    document.write('<table style="margin: 1ex; border: 1px solid grey; padding: 5px;">');
    document.write('<caption></caption>');
    document.write('<colgroup>');
    document.write('<col span="1" style="text-align: right;" />');
    document.write('</colgroup>');

    for (var i = 0; i < conversionsV.Factor.length; i++) {
        document.write("<tr>\n");
        document.write("   <td> " + conversionsV.Factor[i].name  + " </td> \n");
        document.write("   <td> <input type='text' size='50' \n");
        document.write("         onkeyup='convert_volume(this);' \n");
        document.write("         id='" + conversionsV.Factor[i].name + "'> \n");
        document.write("   </td>\n");
        document.write("</tr>\n\n");
    }
    document.write('</table>');
}


/* Convert the input, whatever it is, to meters.
 * Then convert meters to all the possible units.
 * The alternative is to have a whole bunch of conversions for each
 * possible input, which would grow very large.
 */
function convert_volume(item) {
    var input;   // value to be converted
    var numdec;  // how many decimal places we want
    // get value
    if (item.value.length > 0) {
        input = parseFloat(item.value);
    } else {
        // default value if box is empty
        input = 0;
    }
    // find out how decimal places on the input
    if ( item.value.split('.').length == 1 ) {
        // if no decimal point, default to 3
        numdec = 3;
    } else {
        numdec = item.value.split('.')[1].length;
    }

    // convert the input to meters
    for (var i = 0; i < conversionsV.Factor.length; i++) {
        if (conversionsV.Factor[i].name == item.id) {
            var liters = input * conversionsV.Factor[i].from;
            break;
        }
    }

    /* Fill in the boxes
     * Math.round() converts its argument to an integer.
     * but any number has a "toFixed()" method which lets you specify
     * how many digits you want.
     * DO NOT touch the box the user is currently typing in!
     */
    for (var i=0; i < conversionsV.Factor.length; i++) {
        if (item.id != conversionsV.Factor[i].name)
            document.getElementById(conversionsV.Factor[i].name).value  =
                (liters * conversionsV.Factor[i].to).toFixed(numdec);
    }
}
