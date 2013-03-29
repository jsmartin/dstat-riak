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

**glat** - mean latency for get requests (µs)

**puts** - the number of puts per second

**plat** - mean latency for put requests (µs)



A common thing to do is see how gets & puts are interacting with your disk, netowrk, and cpu utlization:



	dstat -t --riak -n -d -c 5                                                                                                                             
	----system---- ------------riak----------- -net/total- -dsk/total- ----total-cpu-usage----
	     time     | gets   glat   puts   plat | recv  send| read  writ|usr sys idl wai hiq siq
	29-03 00:16:25|     0   1136      0   1695|   0     0 |2040B   93k|  2   0  98   0   0   0
	29-03 00:16:30|     0   1134      0   1695| 360B  842B|   0    23k|  0   0 100   0   0   0
	29-03 00:16:35|     0   1131      0   1690|1025B 1324B|   0     0 |  0   0 100   0   0   0
	29-03 00:16:40|    19   1136     14   1699|  34k   33k|   0     0 |  4   3  92   0   0   0
	29-03 00:16:45|    38   1147     23   1714|  78k   77k|   0    54k|  8   6  85   0   0   0
	29-03 00:16:50|    39   1157     23   1726|  79k   73k|   0    29k|  9   6  85   0   0   0
	29-03 00:16:55|    39   1157     23   1730|  80k   75k|   0    21k|  9   7  84   0   0   0
	29-03 00:17:00|    78   1143     49   1718| 156k  147k|   0    18k| 16  13  70   0   0   0
	29-03 00:17:05|    80   1139     48   1707| 163k  149k|   0    25k| 17  13  71   0   0   0
	29-03 00:17:10|    80   1133     53   1697| 165k  154k|   0   135k| 16  12  71   0   0   0
	29-03 00:17:15|    74   1127     46   1688| 160k  148k|   0    46k| 16  12  73   0   0   0
	29-03 00:17:20|    37   1132     23   1691|  76k   72k|   0    84k|  8   6  85   0   0   0
	29-03 00:17:25|    38   1134     26   1693|  76k   73k|   0    30k|  8   6  85   0   0   0
	29-03 00:17:30|    38   1135     25   1694|  78k   75k|   0    19k|  8   7  85   0   0   0
	29-03 00:17:35|    15   1136     10   1695|  39k   37k|   0    18k|  3   3  94   0   0   0
	29-03 00:17:40|     0   1135      0   1694| 239B  558B|   0  6554B|  0   0 100   0   0   0
