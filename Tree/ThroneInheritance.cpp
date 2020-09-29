#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using std::string;
using std::vector;
using std::unordered_map;


// struct Person {
//     string val;
//     vector<Person*> children;
//     bool state;
//     Person(string x) : val(x), state(true) {}
// };

class Person{
public:
    string val;
    bool state = true;
    vector<Person*> children;
    Person(string x){
        val = x;
    }
};

class ThroneInheritance {
    Person* root;
    unordered_map<string, Person*> m;
public:
    ThroneInheritance(string kingName) {
        root = new Person(kingName);
        m[kingName] = root;
    }
    
    void birth(string parentName, string childName) {
        unordered_map<string, Person*>::const_iterator got = m.find(parentName);
        if (got == m.end()) return;
        Person* child = new Person(childName);
        got->second->children.push_back(child);
        m[childName] = child;
    }
    
    void death(string name) {
        unordered_map<string, Person*>::const_iterator got = m.find(name);
        if (got == m.end()) return;
        got->second->state = false;
    }

    void preorder(Person* root, vector<string>& res) {
        if (!root) return;
        if (root->state) res.push_back(root->val);
        for (auto child : root->children)
            preorder(child, res);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> res;
        preorder(root, res);
        return res;
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */