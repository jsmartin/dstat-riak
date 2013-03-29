dstat-riak
==========

A dstat plugin for Riak


first install dstat :)

	apt-get install dstat

or

	yum install dstat

copy dstat-riak.py to a valid directory.  We'll copy it to home for the example.

    git clone https://github.com/jsmartin/dstat-riak
    mkdir $HOME/.dstat
    cp dstat-riak/dstat-riak.py $HOME/.dstat


Make sure Riak is listening on 127.0.0.1:8098 for HTTP requests (you can have a list of IPs & ports)

edit /etc/riak/app.config

    %% http is a list of IP addresses and TCP ports that the Riak
    %% HTTP interface will bind.
    {http, [ {"127.0.0.1", 8098 } ]},

Restart Riak if any changes were made.

run dstat with an interval of 5.  Riak does only updates its stats counters to the HTTP stats interface every 5 seconds.


	  dstat --riak 5                                                                
		-------riak------
		 gets  glat  puts  plat
		    0     0     0     0
		    0     0     0     0
		   34  1240    23  2051
		   38  1204    22  1877
		   37  1197    24  1822
		   38  1195    22  1792
		   38  1192    23  1782
		   37  1189    24  1775
		   38  1187    26  1769
		   27  1185    18  1767
		    0  1185     0  1767
		    0  1185     0  1767
		    
**gets** - the number of gets per second

**glat** - mean latency for get requests (ms)

**puts** - the number of puts per second

**plat** - mean latency for put requests (ms)
