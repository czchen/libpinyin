# -*- coding: utf-8 -*-
# vim:set et sts=4 sw=4:
#
# libpinyin - Library to deal with pinyin.
#
# Copyright (c) 2010 BYVoid <byvoid1@gmail.com>
# Copyright (C) 2011 Peng Wu <alexepico@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.


'''
const static gunichar bopomofo_char[] = {
    L'\0',L'ㄅ',L'ㄆ',L'ㄇ',L'ㄈ',L'ㄉ',L'ㄊ',L'ㄋ',L'ㄌ',L'ㄍ',L'ㄎ',
    L'ㄏ',L'ㄐ',L'ㄑ',L'ㄒ',L'ㄓ',L'ㄔ',L'ㄕ',L'ㄖ',L'ㄗ',L'ㄘ',L'ㄙ',

    L'ㄧ',L'ㄨ',L'ㄩ',L'ㄚ',L'ㄛ',L'ㄜ',L'ㄝ',L'ㄞ',L'ㄟ',L'ㄠ',L'ㄡ',
    L'ㄢ',L'ㄣ',L'ㄤ',L'ㄥ',L'ㄦ',

    L'ˊ',L'ˇ',L'ˋ',L'˙',
};
'''

BOPOMOFO_PINYIN_MAP = {
    "ㄅ" : "b",
    "ㄅㄚ" : "ba",
    "ㄅㄛ" : "bo",
    "ㄅㄞ" : "bai",
    "ㄅㄟ" : "bei",
    "ㄅㄠ" : "bao",
    "ㄅㄢ" : "ban",
    "ㄅㄣ" : "ben",
    "ㄅㄤ" : "bang",
    "ㄅㄥ" : "beng",
    "ㄅㄧ" : "bi",
    "ㄅㄧㄝ" : "bie",
    "ㄅㄧㄠ" : "biao",
    "ㄅㄧㄢ" : "bian",
    "ㄅㄧㄣ" : "bin",
    "ㄅㄧㄥ" : "bing",
    "ㄅㄨ" : "bu",
    "ㄆ" : "p",
    "ㄆㄚ" : "pa",
    "ㄆㄛ" : "po",
    "ㄆㄞ" : "pai",
    "ㄆㄟ" : "pei",
    "ㄆㄠ" : "pao",
    "ㄆㄡ" : "pou",
    "ㄆㄢ" : "pan",
    "ㄆㄣ" : "pen",
    "ㄆㄤ" : "pang",
    "ㄆㄥ" : "peng",
    "ㄆㄧ" : "pi",
    "ㄆㄧㄝ" : "pie",
    "ㄆㄧㄠ" : "piao",
    "ㄆㄧㄢ" : "pian",
    "ㄆㄧㄣ" : "pin",
    "ㄆㄧㄥ" : "ping",
    "ㄆㄨ" : "pu",
    "ㄇ" : "m",
    "ㄇㄚ" : "ma",
    "ㄇㄛ" : "mo",
    "ㄇㄜ" : "me",
    "ㄇㄞ" : "mai",
    "ㄇㄟ" : "mei",
    "ㄇㄠ" : "mao",
    "ㄇㄡ" : "mou",
    "ㄇㄢ" : "man",
    "ㄇㄣ" : "men",
    "ㄇㄤ" : "mang",
    "ㄇㄥ" : "meng",
    "ㄇㄧ" : "mi",
    "ㄇㄧㄝ" : "mie",
    "ㄇㄧㄠ" : "miao",
    "ㄇㄧㄡ" : "miu",
    "ㄇㄧㄢ" : "mian",
    "ㄇㄧㄣ" : "min",
    "ㄇㄧㄥ" : "ming",
    "ㄇㄨ" : "mu",
    "ㄈ" : "f",
    "ㄈㄚ" : "fa",
    "ㄈㄛ" : "fo",
    "ㄈㄜ" : "fe",
    "ㄈㄟ" : "fei",
    "ㄈㄡ" : "fou",
    "ㄈㄢ" : "fan",
    "ㄈㄣ" : "fen",
    "ㄈㄤ" : "fang",
    "ㄈㄥ" : "feng",
    "ㄈㄨ" : "fu",
    "ㄉ" : "d",
    "ㄉㄚ" : "da",
    "ㄉㄜ" : "de",
    "ㄉㄞ" : "dai",
    "ㄉㄟ" : "dei",
    "ㄉㄠ" : "dao",
    "ㄉㄡ" : "dou",
    "ㄉㄢ" : "dan",
    "ㄉㄣ" : "den",
    "ㄉㄤ" : "dang",
    "ㄉㄥ" : "deng",
    "ㄉㄧ" : "di",
    "ㄉㄧㄚ" : "dia",
    "ㄉㄧㄝ" : "die",
    "ㄉㄧㄠ" : "diao",
    "ㄉㄧㄡ" : "diu",
    "ㄉㄧㄢ" : "dian",
    "ㄉㄧㄣ" : "din",
    "ㄉㄧㄥ" : "ding",
    "ㄉㄨ" : "du",
    "ㄉㄨㄛ" : "duo",
    "ㄉㄨㄟ" : "dui",
    "ㄉㄨㄢ" : "duan",
    "ㄉㄨㄣ" : "dun",
    "ㄉㄨㄥ" : "dong",
    "ㄊ" : "t",
    "ㄊㄚ" : "ta",
    "ㄊㄜ" : "te",
    "ㄊㄞ" : "tai",
    "ㄊㄠ" : "tao",
    "ㄊㄡ" : "tou",
    "ㄊㄢ" : "tan",
    "ㄊㄤ" : "tang",
    "ㄊㄥ" : "teng",
    "ㄊㄧ" : "ti",
    "ㄊㄧㄝ" : "tie",
    "ㄊㄧㄠ" : "tiao",
    "ㄊㄧㄢ" : "tian",
    "ㄊㄧㄥ" : "ting",
    "ㄊㄨ" : "tu",
    "ㄊㄨㄛ" : "tuo",
    "ㄊㄨㄟ" : "tui",
    "ㄊㄨㄢ" : "tuan",
    "ㄊㄨㄣ" : "tun",
    "ㄊㄨㄥ" : "tong",
    "ㄋ" : "n",
    "ㄋㄚ" : "na",
    "ㄋㄜ" : "ne",
    "ㄋㄞ" : "nai",
    "ㄋㄟ" : "nei",
    "ㄋㄠ" : "nao",
    "ㄋㄡ" : "nou",
    "ㄋㄢ" : "nan",
    "ㄋㄣ" : "nen",
    "ㄋㄤ" : "nang",
    "ㄋㄥ" : "neng",
    "ㄋㄧ" : "ni",
    "ㄋㄧㄚ" : "nia",
    "ㄋㄧㄝ" : "nie",
    "ㄋㄧㄠ" : "niao",
    "ㄋㄧㄡ" : "niu",
    "ㄋㄧㄢ" : "nian",
    "ㄋㄧㄣ" : "nin",
    "ㄋㄧㄤ" : "niang",
    "ㄋㄧㄥ" : "ning",
    "ㄋㄨ" : "nu",
    "ㄋㄨㄛ" : "nuo",
    "ㄋㄨㄢ" : "nuan",
    "ㄋㄨㄣ" : "nun",
    "ㄋㄨㄥ" : "nong",
    "ㄋㄩ" : "nv",
    "ㄋㄩㄝ" : "nve",
    "ㄌ" : "l",
    "ㄌㄚ" : "la",
    "ㄌㄛ" : "lo",
    "ㄌㄜ" : "le",
    "ㄌㄞ" : "lai",
    "ㄌㄟ" : "lei",
    "ㄌㄠ" : "lao",
    "ㄌㄡ" : "lou",
    "ㄌㄢ" : "lan",
    "ㄌㄣ" : "len",
    "ㄌㄤ" : "lang",
    "ㄌㄥ" : "leng",
    "ㄌㄧ" : "li",
    "ㄌㄧㄚ" : "lia",
    "ㄌㄧㄝ" : "lie",
    "ㄌㄧㄠ" : "liao",
    "ㄌㄧㄡ" : "liu",
    "ㄌㄧㄢ" : "lian",
    "ㄌㄧㄣ" : "lin",
    "ㄌㄧㄤ" : "liang",
    "ㄌㄧㄥ" : "ling",
    "ㄌㄨ" : "lu",
    "ㄌㄨㄛ" : "luo",
    "ㄌㄨㄢ" : "luan",
    "ㄌㄨㄣ" : "lun",
    "ㄌㄨㄥ" : "long",
    "ㄌㄩ" : "lv",
    "ㄌㄩㄝ" : "lve",
    "ㄍ" : "g",
    "ㄍㄚ" : "ga",
    "ㄍㄜ" : "ge",
    "ㄍㄞ" : "gai",
    "ㄍㄟ" : "gei",
    "ㄍㄠ" : "gao",
    "ㄍㄡ" : "gou",
    "ㄍㄢ" : "gan",
    "ㄍㄣ" : "gen",
    "ㄍㄤ" : "gang",
    "ㄍㄥ" : "geng",
    "ㄍㄨ" : "gu",
    "ㄍㄨㄚ" : "gua",
    "ㄍㄨㄛ" : "guo",
    "ㄍㄨㄞ" : "guai",
    "ㄍㄨㄟ" : "gui",
    "ㄍㄨㄢ" : "guan",
    "ㄍㄨㄣ" : "gun",
    "ㄍㄨㄤ" : "guang",
    "ㄍㄨㄥ" : "gong",
    "ㄎ" : "k",
    "ㄎㄚ" : "ka",
    "ㄎㄜ" : "ke",
    "ㄎㄞ" : "kai",
    "ㄎㄟ" : "kei",
    "ㄎㄠ" : "kao",
    "ㄎㄡ" : "kou",
    "ㄎㄢ" : "kan",
    "ㄎㄣ" : "ken",
    "ㄎㄤ" : "kang",
    "ㄎㄥ" : "keng",
    "ㄎㄨ" : "ku",
    "ㄎㄨㄚ" : "kua",
    "ㄎㄨㄛ" : "kuo",
    "ㄎㄨㄞ" : "kuai",
    "ㄎㄨㄟ" : "kui",
    "ㄎㄨㄢ" : "kuan",
    "ㄎㄨㄣ" : "kun",
    "ㄎㄨㄤ" : "kuang",
    "ㄎㄨㄥ" : "kong",
    "ㄏ" : "h",
    "ㄏㄚ" : "ha",
    "ㄏㄜ" : "he",
    "ㄏㄞ" : "hai",
    "ㄏㄟ" : "hei",
    "ㄏㄠ" : "hao",
    "ㄏㄡ" : "hou",
    "ㄏㄢ" : "han",
    "ㄏㄣ" : "hen",
    "ㄏㄤ" : "hang",
    "ㄏㄥ" : "heng",
    "ㄏㄨ" : "hu",
    "ㄏㄨㄚ" : "hua",
    "ㄏㄨㄛ" : "huo",
    "ㄏㄨㄞ" : "huai",
    "ㄏㄨㄟ" : "hui",
    "ㄏㄨㄢ" : "huan",
    "ㄏㄨㄣ" : "hun",
    "ㄏㄨㄤ" : "huang",
    "ㄏㄨㄥ" : "hong",
    "ㄐ" : "j",
    "ㄐㄧ" : "ji",
    "ㄐㄧㄚ" : "jia",
    "ㄐㄧㄝ" : "jie",
    "ㄐㄧㄠ" : "jiao",
    "ㄐㄧㄡ" : "jiu",
    "ㄐㄧㄢ" : "jian",
    "ㄐㄧㄣ" : "jin",
    "ㄐㄧㄤ" : "jiang",
    "ㄐㄧㄥ" : "jing",
    "ㄐㄩ" : "ju",
    "ㄐㄩㄝ" : "jue",
    "ㄐㄩㄢ" : "juan",
    "ㄐㄩㄣ" : "jun",
    "ㄐㄩㄥ" : "jiong",
    "ㄑ" : "q",
    "ㄑㄧ" : "qi",
    "ㄑㄧㄚ" : "qia",
    "ㄑㄧㄝ" : "qie",
    "ㄑㄧㄠ" : "qiao",
    "ㄑㄧㄡ" : "qiu",
    "ㄑㄧㄢ" : "qian",
    "ㄑㄧㄣ" : "qin",
    "ㄑㄧㄤ" : "qiang",
    "ㄑㄧㄥ" : "qing",
    "ㄑㄩ" : "qu",
    "ㄑㄩㄝ" : "que",
    "ㄑㄩㄢ" : "quan",
    "ㄑㄩㄣ" : "qun",
    "ㄑㄩㄥ" : "qiong",
    "ㄒ" : "x",
    "ㄒㄧ" : "xi",
    "ㄒㄧㄚ" : "xia",
    "ㄒㄧㄝ" : "xie",
    "ㄒㄧㄠ" : "xiao",
    "ㄒㄧㄡ" : "xiu",
    "ㄒㄧㄢ" : "xian",
    "ㄒㄧㄣ" : "xin",
    "ㄒㄧㄤ" : "xiang",
    "ㄒㄧㄥ" : "xing",
    "ㄒㄩ" : "xu",
    "ㄒㄩㄝ" : "xue",
    "ㄒㄩㄢ" : "xuan",
    "ㄒㄩㄣ" : "xun",
    "ㄒㄩㄥ" : "xiong",
    "ㄓ" : "zhi",
    "ㄓㄚ" : "zha",
    "ㄓㄜ" : "zhe",
    "ㄓㄞ" : "zhai",
    "ㄓㄟ" : "zhei",
    "ㄓㄠ" : "zhao",
    "ㄓㄡ" : "zhou",
    "ㄓㄢ" : "zhan",
    "ㄓㄣ" : "zhen",
    "ㄓㄤ" : "zhang",
    "ㄓㄥ" : "zheng",
    "ㄓㄨ" : "zhu",
    "ㄓㄨㄚ" : "zhua",
    "ㄓㄨㄛ" : "zhuo",
    "ㄓㄨㄞ" : "zhuai",
    "ㄓㄨㄟ" : "zhui",
    "ㄓㄨㄢ" : "zhuan",
    "ㄓㄨㄣ" : "zhun",
    "ㄓㄨㄤ" : "zhuang",
    "ㄓㄨㄥ" : "zhong",
    "ㄔ" : "chi",
    "ㄔㄚ" : "cha",
    "ㄔㄜ" : "che",
    "ㄔㄞ" : "chai",
    "ㄔㄠ" : "chao",
    "ㄔㄡ" : "chou",
    "ㄔㄢ" : "chan",
    "ㄔㄣ" : "chen",
    "ㄔㄤ" : "chang",
    "ㄔㄥ" : "cheng",
    "ㄔㄨ" : "chu",
    "ㄔㄨㄚ" : "chua",
    "ㄔㄨㄛ" : "chuo",
    "ㄔㄨㄞ" : "chuai",
    "ㄔㄨㄟ" : "chui",
    "ㄔㄨㄢ" : "chuan",
    "ㄔㄨㄣ" : "chun",
    "ㄔㄨㄤ" : "chuang",
    "ㄔㄨㄥ" : "chong",
    "ㄕ" : "shi",
    "ㄕㄚ" : "sha",
    "ㄕㄜ" : "she",
    "ㄕㄞ" : "shai",
    "ㄕㄟ" : "shei",
    "ㄕㄠ" : "shao",
    "ㄕㄡ" : "shou",
    "ㄕㄢ" : "shan",
    "ㄕㄣ" : "shen",
    "ㄕㄤ" : "shang",
    "ㄕㄥ" : "sheng",
    "ㄕㄨ" : "shu",
    "ㄕㄨㄚ" : "shua",
    "ㄕㄨㄛ" : "shuo",
    "ㄕㄨㄞ" : "shuai",
    "ㄕㄨㄟ" : "shui",
    "ㄕㄨㄢ" : "shuan",
    "ㄕㄨㄣ" : "shun",
    "ㄕㄨㄤ" : "shuang",
    "ㄖ" : "ri",
    "ㄖㄜ" : "re",
    "ㄖㄠ" : "rao",
    "ㄖㄡ" : "rou",
    "ㄖㄢ" : "ran",
    "ㄖㄣ" : "ren",
    "ㄖㄤ" : "rang",
    "ㄖㄥ" : "reng",
    "ㄖㄨ" : "ru",
    "ㄖㄨㄚ" : "rua",
    "ㄖㄨㄛ" : "ruo",
    "ㄖㄨㄟ" : "rui",
    "ㄖㄨㄢ" : "ruan",
    "ㄖㄨㄣ" : "run",
    "ㄖㄨㄥ" : "rong",
    "ㄗ" : "zi",
    "ㄗㄚ" : "za",
    "ㄗㄜ" : "ze",
    "ㄗㄞ" : "zai",
    "ㄗㄟ" : "zei",
    "ㄗㄠ" : "zao",
    "ㄗㄡ" : "zou",
    "ㄗㄢ" : "zan",
    "ㄗㄣ" : "zen",
    "ㄗㄤ" : "zang",
    "ㄗㄥ" : "zeng",
    "ㄗㄨ" : "zu",
    "ㄗㄨㄛ" : "zuo",
    "ㄗㄨㄟ" : "zui",
    "ㄗㄨㄢ" : "zuan",
    "ㄗㄨㄣ" : "zun",
    "ㄗㄨㄥ" : "zong",
    "ㄘ" : "ci",
    "ㄘㄚ" : "ca",
    "ㄘㄜ" : "ce",
    "ㄘㄞ" : "cai",
    "ㄘㄠ" : "cao",
    "ㄘㄡ" : "cou",
    "ㄘㄢ" : "can",
    "ㄘㄣ" : "cen",
    "ㄘㄤ" : "cang",
    "ㄘㄥ" : "ceng",
    "ㄘㄨ" : "cu",
    "ㄘㄨㄛ" : "cuo",
    "ㄘㄨㄟ" : "cui",
    "ㄘㄨㄢ" : "cuan",
    "ㄘㄨㄣ" : "cun",
    "ㄘㄨㄥ" : "cong",
    "ㄙ" : "si",
    "ㄙㄚ" : "sa",
    "ㄙㄜ" : "se",
    "ㄙㄞ" : "sai",
    "ㄙㄠ" : "sao",
    "ㄙㄡ" : "sou",
    "ㄙㄢ" : "san",
    "ㄙㄣ" : "sen",
    "ㄙㄤ" : "sang",
    "ㄙㄥ" : "seng",
    "ㄙㄨ" : "su",
    "ㄙㄨㄛ" : "suo",
    "ㄙㄨㄟ" : "sui",
    "ㄙㄨㄢ" : "suan",
    "ㄙㄨㄣ" : "sun",
    "ㄙㄨㄥ" : "song",
    "ㄚ" : "a",
    "ㄛ" : "o",
    "ㄜ" : "e",
    "ㄞ" : "ai",
    "ㄟ" : "ei",
    "ㄠ" : "ao",
    "ㄡ" : "ou",
    "ㄢ" : "an",
    "ㄣ" : "en",
    "ㄤ" : "ang",
    "ㄥ" : "eng",
    "ㄦ" : "er",
    "ㄧ" : "yi",
    "ㄧㄚ" : "ya",
    "ㄧㄛ" : "yo",
    "ㄧㄝ" : "ye",
    "ㄧㄞ" : "yai",
    "ㄧㄠ" : "yao",
    "ㄧㄡ" : "you",
    "ㄧㄢ" : "yan",
    "ㄧㄣ" : "yin",
    "ㄧㄤ" : "yang",
    "ㄧㄥ" : "ying",
    "ㄨ" : "wu",
    "ㄨㄚ" : "wa",
    "ㄨㄛ" : "wo",
    "ㄨㄞ" : "wai",
    "ㄨㄟ" : "wei",
    "ㄨㄢ" : "wan",
    "ㄨㄣ" : "wen",
    "ㄨㄤ" : "wang",
    "ㄨㄥ" : "weng",
    "ㄩ" : "yu",
    "ㄩㄝ" : "yue",
    "ㄩㄢ" : "yuan",
    "ㄩㄣ" : "yun",
    "ㄩㄥ" : "yong",
    "ㄫ" : "ng",
}

PINYIN_BOPOMOFO_MAP = dict([(v, k) for k, v in BOPOMOFO_PINYIN_MAP.items()])

SHENG_YUN_BOPOMOFO_MAP = {
    "b" : "ㄅ",
    "p" : "ㄆ",
    "m" : "ㄇ",
    "f" : "ㄈ",
    "d" : "ㄉ",
    "t" : "ㄊ",
    "n" : "ㄋ",
    "l" : "ㄌ",
    "g" : "ㄍ",
    "k" : "ㄎ",
    "h" : "ㄏ",
    "j" : "ㄐ",
    "q" : "ㄑ",
    "x" : "ㄒ",
    "zh" : "ㄓ",
    "ch" : "ㄔ",
    "sh" : "ㄕ",
    "r" : "ㄖ",
    "z" : "ㄗ",
    "c" : "ㄘ",
    "s" : "ㄙ",

    # 韻母為u,ue,un,uan,ong時ㄧ省略
    "y" : ("ㄧ", (("u", "ue", "un", "uan", "ong"), "")),
    "w" : "ㄨ",
    "a" : "ㄚ",
    "o" : "ㄛ",
    "e" : ("ㄜ", ("y", "ㄝ")),  # y後面為ㄝ

    # zh ch sh r z c s y後面為空
    "i" : ("ㄧ", (("zh", "ch", "sh", "r", "z", "c", "s", "y"), "")),

    # jqxy後面為ㄩ w後面為空
    "u" : ("ㄨ", ("jqxy", "ㄩ")),
    "v" : "ㄩ",
    "ai" : "ㄞ",
    "ei" : "ㄟ",
    "ao" : "ㄠ",
    "ou" : "ㄡ",
    "an" : "ㄢ",
    "en" : "ㄣ",
    "ang" : "ㄤ",
    "eng" : "ㄥ",
    "er" : "ㄦ",
    "ia" : "ㄧㄚ",
    "ie" : "ㄧㄝ",
    "iai" : "ㄧㄞ",
    "iao" : "ㄧㄠ",
    "iu" : "ㄧㄡ",
    "ian" : "ㄧㄢ",
    "in" : ("ㄧㄣ", ("y", "ㄣ")),      #y後面為ㄣ
    "iang" : "ㄧㄤ",
    "ing" : ("ㄧㄥ", ("y", "ㄥ")),     #y後面為ㄥ
    "ua" : "ㄨㄚ",
    "uo" : "ㄨㄛ",
    "ue" : "ㄩㄝ",
    # TODO: "ve" is OK?
    "ve" : "ㄩㄝ",
    "uai" : "ㄨㄞ",
    "ui" : "ㄨㄟ",
    "uan" :  ("ㄨㄢ", ("jqxy", "ㄩㄢ")),  # jqxy後面是ㄩㄢ
    "un" :   ("ㄨㄣ", ("jqxy", "ㄩㄣ")),  # jqxy後面是ㄩㄣ
    "uang" : ("ㄨㄤ", ("jqxy", "ㄩㄤ")),  # jqxy後面是ㄩㄤ
    "ong" :  ("ㄨㄥ", ("jqxy", "ㄩㄥ")),  # y後面為ㄩㄥ
    "iong" : "ㄩㄥ",
}
