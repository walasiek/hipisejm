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
        wget --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36" "https://httpbin.io/user-agent" "$URL"
    fi
    cd $CUR_DIR
}

# updated 2024-06-19

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

# posiedzenie 7
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/B16EF42E15649275C1258AD80083078A/%24File/07_a_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/AE12C6BC9F43141FC1258ADA000817E9/%24File/07_b_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/DED92587B3019456C1258ADA00540928/%24File/07_c_ksiazka_bis.pdf

# posiedzenie 8
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/200A2BAA707A2D95C1258AE600775320/%24File/08_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/0D28AED4D7D5D1D2C1258AE700671747/%24File/08_b_ksiazka.pdf

# posiedzenie 9
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/3D1D243C6084DB49C1258AFB0078C0AD/%24File/09_a_ksiazka_bis.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/0A90B1DBFB57A5D0C1258AFC00750D36/%24File/09_b_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/F60A3A74B0945F4BC1258AFD0063BD4E/%24File/09_c_ksiazka.pdf

# posiedzenie 10
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/91C08D7AA3F4475FC1258B090076D0D8/%24File/10_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/9EF353A76A58A1EEC1258B0A00695D00/%24File/10_b_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/732B6299E35C2031C1258B0B00668847/%24File/10_c_ksiazka.pdf

# posiedzenie 11
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/5C5E8620CF0AC49DC1258B1700751E8E/%24File/11_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/3ED1126B70C40177C1258B19000127CE/%24File/11_b_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/92E9C717C85A0710C1258B1E0078E463/%24File/11_c_ksiazka.pdf

# posiedzenie 12
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/0A9796C81781FB60C1258B25007A7C71/%24File/12_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/9923CDFE90B4E5E7C1258B2600651B76/%24File/12_b_ksiazka.pdf

# posiedzenie 13
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/4565D787BA9F38D1C1258B3A006327E9/%24File/13_a_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/444A16C0227EA306C1258B3B00732E4B/%24File/13_b_ksiazka.pdf
download_url http://orka2.sejm.gov.pl/StenoInter10.nsf/0/A87D81B062B7FC5EC1258B3C004CC62F/%24File/13_c_ksiazka.pdf

# posiedzenie 14
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/EAF0B6AB89A9E74DC1258B4800805E7C/%24File/14_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/38DF3ECD6B59ACFEC1258B490071AEF9/%24File/14_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/9EF8DF4DBC1097A4C1258B4A005BA0CF/%24File/14_c_ksiazka.pdf

# posiedzenie 15
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/3129A6E257852A68C1258B57007DE3DB/%24File/15_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/AE7D836903477314C1258B58006AC348/%24File/15_b_ksiazka.pdf

# posiedzenie 16
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/7285C41C280CD613C1258B63007694C7/%24File/16_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/2F4749862D334FEFC1258B64007B4C2E/%24File/16_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/FE25165C606CA4A7C1258B650073F383/%24File/16_c_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/15ADEE9FDCDD99C2C1258B66007356F9/%24File/16_d_ksiazka.pdf

# posiedzenie 17
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/8AE3C0C231CC6EA4C1258B95006D00E5/%24File/17_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/B507B83A9C0822ADC1258B9600764B3E/%24File/17_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/0DF2E7CD56E4BD31C1258B97006B4073/%24File/17_c_ksiazka.pdf

# posiedzenie 18
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/50A534C6B81DBA71C1258BA40008C629/%24File/18_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/E674BFADC8BDAFABC1258BA5000129EB/%24File/18_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/7A38CDDC05426116C1258BA5006EBDC0/%24File/18_c_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/B985B70BC9DF60A3C1258BA900740573/%24File/18_d_ksiazka.pdf

# posiedzenie 19
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/217BE29605146D4FC1258BB1006492E3/%24File/19_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/0449D264AD37B58EC1258BB2007C4D9A/%24File/19_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/BE4FFB681F7F75A3C1258BB30064CA2D/%24File/19_c_ksiazka.pdf

# posiedzenie 20
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/DBE1FE43BDC6F4F3C1258BB80066387D/%24File/20_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/20DB3CEDA9FC4B15C1258BB9006C0B16/%24File/20_b_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/7DFC26BA801B4983C1258BBA0053C352/%24File/20_c_ksiazka.pdf

# posiedzenie 21
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/D18F5B664B4137D7C1258BCE00021143/%24File/21_a_ksiazka.pdf
download_url https://orka2.sejm.gov.pl/StenoInter10.nsf/0/6FD4DB5238E00553C1258BCF0002992E/%24File/21_b_ksiazka.pdf
