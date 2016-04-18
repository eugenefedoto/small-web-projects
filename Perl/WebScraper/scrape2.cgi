#! /usr/bin/perl -w

# Scrape2.cgi - demonstrate screen-scraping in Perl
#               this one follows a link
# Eugene A. Fedotov
#

use strict;
use CGI;
use WWW::Mechanize;
use HTML::TokeParser;
use DateTime;



# URLs look like: http://www.penny-arcade.com/comic/2015/02/27/

my $date = DateTime->now;

while ( $date->day_of_week != 1 ) {
    $date->subtract( days => 1 );
}

$date->subtract(days => 21);

# format the date the way the URL needs to look:

my $target = sprintf("%04d/%02d/%02d", $date->year(), $date->month(), $date->day());

# fetch the data:
my $agent = WWW::Mechanize->new();
$agent->get('http://www.penny-arcade.com/comic/' . $target) ;
my $stream = HTML::TokeParser->new(\$agent->{content});
my $cgi = new CGI;
sub create_cartoons{ # one parameter to indicate number of cartoons

	# First, get the cartoon:

	my $tag = $stream->get_tag("a");

	while ($tag->[1]{title} and $tag->[1]{title} ne 'Next'){
	    $tag = $stream->get_tag("a");
	}

	my $toon = $stream->get_tag("img");

	# get attribute:
	my $source = $toon->[1]{'src'};

	# create CGI object and generate HTML:



	print $cgi->header( type=>'text/html'),
	      $cgi->start_html("Penny Arcade Screen Scrape");
	print $cgi->img({src=>$source}), "\n\n";

	for (my $i=0; $i < $_[0]-1; $i++) {
		$agent->follow_link(text => 'Next');
		$stream = HTML::TokeParser->new(\$agent->{content});

		$tag = $stream->get_tag("a");

		while ($tag->[1]{title} and $tag->[1]{title} ne 'Next'){
		    $tag = $stream->get_tag("a");
		}

		$toon = $stream->get_tag("img");

		$source = $toon->[1]{'src'};
		print $cgi->img({src=>$source}), "\n\n";
	}
}



&create_cartoons(3); # param = num of cartoons

# ALL DONE!
print $cgi->end_html, "\n";
