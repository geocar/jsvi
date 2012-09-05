#!/usr/bin/perl
use Lingua::Ispell;
use CGI qw/:standard/;

print "Content-Type: text/plain; charset=UTF-8\n\n";
print STDERR "tick\n";
foreach my $i (param()) {
	if ($i =~ /^a/) {
		my $w = param($i);
		print STDERR "add to dictionary: $w\n";
	} elsif ($i =~ /^c/) {
		my $w = param($i);
		my ($r)=(Lingua::Ispell::spellcheck(lc($w)));
		if ($r->{type} eq 'ok' || $r->{type} eq '') {
			print "$i=$w\n";
		} elsif ($r->{type} eq 'root') {
			print "$i=$w\n";
		} elsif ($r->{type} eq 'miss') {
			print "$i=\n";
			foreach my $j (@{ $r->{misses} }) {
				print "$i=$j\n";
			}
		} elsif ($r->{type} eq 'guess') {
			print "$i=\n";
			foreach my $j (@{ $r->{guesses} }) {
				print "$i=$j\n";
			}
		} elsif ($r->{type} eq 'compound') {
			print "$i=$i\n";
		} elsif ($r->{type} eq 'none') {
			print "$i=\n";
		}
	}
}




