#pragma once
#include <string>
#include <vector>
#include<iostream>


// From a string s and given a set of character s_s considered as seprator,
// returns a vector of string for each substring in s separeted by 
// at least one character in s_s 
std::vector<std::string> split(const std::string& s, const std::string& s_s);


