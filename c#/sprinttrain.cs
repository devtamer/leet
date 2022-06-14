 var incr = new int[n + 2];
        for (int i = 0; i < routes.Length - 1; i++){
            var start = Math.Min(routes[i], routes[i+1]);
            var end = Math.Max(routes[i], routes[i+1]);
            incr[start]++;
            incr[end+1]--;
        }
        var markers = new int[n+1];
        var markerC = 0;
        for (int i=1; i<n+1; i++){
            markerC += incr[i];
            markers[i] = score;
        }
        var result = new KeyValuePair<int, int>(0, 0 );
        for(int i = 1; i < n+1; i++){
            if (markers[i] < result.Value){
                result = new KeyValuePair<int, int>(i, markers[i]);
                
            }
        }
        return result.Key;