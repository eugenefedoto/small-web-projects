#!/usr/bin/perl -wT

use strict;
use CGI qw(:standard);
my($string, $number, $color, $style) = (param("string"), param("number"), param("color"), param("style"));

print header();
print start_html("CGI Count to Ten");
if ($style) {
    print p(b($string));
} else {
    print p($string);
}
for (my $i = 0; $i < 10; $i++) {
    if ($color eq "red") {
        print p(font({
            -color => "red"
		     }, $number + $i));
    }
    elsif($color eq "blue") {
        print p(font({
            -color => "blue"
		     }, $number + $i));
    } else {
        print p(font({
            -color => "green"
		     }, $number + $i));
    }
}
print end_html;
