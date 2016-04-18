#!/usr/bin/perl -w
use strict;
use WWW::Mechanize;
use HTML::TokeParser;
use CGI;

my $agent = WWW::Mechanize->new();
$agent->get("http://www.penny-arcade.com/comic");
my $stream = HTML::TokeParser->new(\$agent->{content});
my $tag = $stream->get_tag("div");

while ($tag->[1]{class} and $tag->[1]{class} ne "copy ComicTag") {
    $tag = $stream->get_tag("div");
}

$tag = $stream->get_tag("h4");
$tag = $stream->get_tag("h2");
my $comic_title = $stream->get_trimmed_text("/h2");

while ($tag->[1]{id} and $tag->[1]{id} ne "comicFrame") {
    $tag = $stream->get_tag("div");
}

$tag = $stream->get_tag("a");
my $toon = $stream->get_tag("img");

my $source = $toon->[1]{'src'};
my $caption = $toon->[1]{'alt'};

my $cgi = new CGI;

print $cgi->header(-type=>'text/html'),
      $cgi->start_html('HW7 Screen Scrape');

print $cgi->h1("$comic_title"), "\n";

print $cgi->img({src=>$source, alt=>$caption}), "\n\n";
$agent->get("http://trenchescomic.com/comic");
$stream = HTML::TokeParser->new(\$agent->{content});
$tag = $stream->get_tag("div");
while ($tag->[1]{class} and $tag->[1]{class} ne "top") {
    $tag = $stream->get_tag("div");
}
$toon = $stream->get_tag("img");
$source = $toon->[1]{'src'};
$caption = $toon->[1]{'alt'};

print $cgi->p($caption), "\n";

print $cgi->img({src=>$source, alt=>$caption}), "\n\n";

$agent->get("http://campcomic.com/comic/");
$stream = HTML::TokeParser->new(\$agent->{content});
$tag = $stream->get_tag("div");
while ($tag->[1]{class} ne "comicMeta") {
    $tag = $stream->get_tag("div");
}
$tag = $stream->get_tag("h1");
$comic_title = $stream->get_trimmed_text("/h1");
while ($tag->[1]{id} ne "comic") {
    $tag = $stream->get_tag("div");
}
$toon = $stream->get_tag("img");
$source = $toon->[1]{'src'};
print $cgi->h1("$comic_title"), "\n";
print $cgi->img({src=>$source, alt=>$caption}), "\n\n";
print $cgi->end_html, "\n";