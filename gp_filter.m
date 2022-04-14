function [pxx_filt] = gp_filter(pxx, q, std_factor)

    pxx_filt = zeros(length(pxx),1);
    an = 1;
    k = 1;
    limit = length(pxx);
    while 1
        an = q^(k - 1);
        if an > limit
            break
        end
        pg(k) = floor(an);
        k = k + 1;
    end

    for i = 1:length(pg)-1
        pxx_fraction = pxx(pg(i):pg(i+1));
        median_filter = medfilt1(pxx_fraction,length(pxx_fraction));
        bad_indexes = abs(pxx_fraction - median_filter) > abs(std(pxx_fraction))/std_factor;
        pxx_fraction(bad_indexes) = median_filter(bad_indexes);
        pxx_filt(pg(i):pg(i+1)) = pxx_fraction;
    end
    pxx_filt(pxx_filt == 0) = [];

end