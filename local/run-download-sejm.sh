#!/bin/bash -e

OUTDIR=resources/raw-data/sejm/

if [[ ! -d $OUTDIR ]]; then
    mkdir -p $OUTDIR
fi

download_url()
{
    URL=$1

    CUR_DIR=`pwd`
    cd $OUTDIR

    OUTFILENAME=`echo "$URL" | sed -r 's/^.*\///;'`

    if [[ -e $OUTFILENAME ]]; then
        echo "$URL already downloaded. Not processing..."
    else
        echo "Download $URL -> $OUTFILENAME"
        wget "$URL"
    fi
    cd $CUR_DIR
}

# updated 2024-03-06

# year 2023
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/C7DCC9BE5661F67FC1258A67007287C0/%24File/01_a_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/2E30269712839930C1258A680032733C/%24File/01_b_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/FDAB9494DE7AAC0AC1258A6E0061446F/%24File/01_c_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/67C3601DEF6387B7C1258A6F0063401F/%24File/01_d_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/E9747D21B438EAA9C1258A760004B869/%24File/01_e_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/5EA2FC331EDABAFDC1258A760079790B/%24File/01_f_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/22D977BD78CAA706C1258A7D00637497/%24File/01_g_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/9475B496D38614E7C1258A7E00783197/%24File/01_h_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/ED3E29043EE0239EC1258A820079BF5A/%24File/01_i_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/E15E9A585B3C9D89C1258A8400038AA5/%24File/01_j_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/A139C44E6F1B62B1C1258A8A0082C4FF/%24File/01_k_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/BA9950BB5E9A57C9C1258A8B007CB398/%24File/01_l_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/3716C01AAB0CE359C1258A8C007C4768/%24File/01_m_ksiazka.pdf

# year 2024

# posiedzenie 2
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/549E67AC4019B62DC1258AA6007A4C96/%24File/02_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/BCB914760793FF62C1258AA70073FB1B/%24File/02_b_ksiazka.pdf

#posiedzenie 3
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/B3A8ADC00D877397C1258AA800524A70/%24File/03_ksiazka.pdf

# posiedzenie 4
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/B21978BF293C4FBAC1258AAF007269AE/%24File/04_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/2819755A64278FABC1258AB0006D099B/%24File/04_b_ksiazka.pdf

# posiedzenie 5
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/FCBB3E6FA72045C2C1258ABC007D889B/%24File/05_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/29036FC0033EAD73C1258ABD007DEBEC/%24File/05_b_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/8641ADF2777C9A5EC1258ABE006B85C9/%24File/05_c_ksiazka.pdf

# posiedzenie 6
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/801CEE318507B4A7C1258ACA006D74AE/%24File/06_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/396CA9723ACCAD51C1258ACC0000B772/%24File/06_b_ksiazka.pdf
