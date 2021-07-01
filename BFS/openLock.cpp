#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
#include <queue>
#include <functional>   // std::greater

using std::string;
using std::vector;
using std::unordered_set;
using std::queue;

struct Astar {
	static int getH(const string& status, const string& target) {
		int ret = 0;
		for (int i = 0; i < 4; ++i)
		{
			int dist = abs(status[i] - target[i]);
			ret += std::min(dist, 10 - dist);
		}
		return ret;
	}

	Astar(const string& status, const string& target, int g) : m_status(status), m_g(g), m_h(getH(status, target)) {
		m_f = m_g + m_h;
	}

	bool operator>(const Astar& that) const {
		return m_f > that.m_f;
	}

	// m_f = m_g + m_h
	string m_status;
	int m_f, m_g, m_h;
};


class Solution {
public:
	int openLock(vector<string>& deadends, string target) {
		if (target == "0000") 
			return 0;

		std::unordered_set<string> dead(deadends.begin(), deadends.end());
		if (dead.find("0000") != dead.end()) 
			return -1;

		auto num_prev = [](char c) -> char {
			return c == '0' ? '9' : c - 1;
		};

		auto num_next = [](char c) -> char {
			return c == '9' ? '0' : c + 1;
		};

		auto move_next = [&](string& status) -> vector<string> {
			vector<string> ret;
			for (int i = 0; i < 4; ++i) {
				char num = status[i];
				status[i] = num_prev(num);
				ret.emplace_back(status);
				status[i] = num_next(num);
				ret.emplace_back(status);
				status[i] = num;
			}
			return ret;
		};

		std::priority_queue<Astar, vector<Astar>, std::greater<Astar>> pq;
		// std::priority_queue<Astar> pq;
		std::unordered_set<string> seen{ "0000" };
		pq.emplace("0000", target, 0);
		while (!pq.empty()) {
			Astar node = pq.top();
			pq.pop();
			for (auto&& str_ : move_next(node.m_status)) {
				if (str_ == target)
					return node.m_g + 1;
				if (dead.find(str_) == dead.end() && seen.find(str_) == seen.end())
				{
					pq.emplace(str_, target, node.m_g + 1);
					seen.insert(std::move(str_));
				}
			}
		}
		return -1;
	}
};


class SolutionBFS {
public:
	string add(string cur, int i) {
		if (cur[i] < '9')
			cur[i] += 1;
		else
			cur[i] = '0';
		return cur;
	}

	string minus(string cur, int i) {
		if (cur[i] > '0')
			cur[i] -= 1;
		else
			cur[i] = '9';
		return cur;
	}

	void move(string& cur, unordered_set<string>& used,
		unordered_set<string>& deadendset, queue<string>& q) {
		for (int i = 0; i < 4; ++i) {
			string a_s = add(cur, i);
			if (used.find(a_s) == used.end() && deadendset.find(a_s) == deadendset.end()) {
				q.push(a_s);
				used.insert(a_s);
			}

			string m_s = minus(cur, i);
			if (used.find(m_s) == used.end() && deadendset.find(m_s) == deadendset.end()) {
				q.push(m_s);
				used.insert(m_s);
			}
		}
	}

	int openLock(vector<string>& deadends, string target) {
		unordered_set<string> used;
		unordered_set<string> deadendset(deadends.begin(), deadends.end());
		queue<string> q;
		if (deadendset.find("0000") != deadendset.end())
			return -1;
		q.emplace("0000");
		int step = 0;
		while (!q.empty()) {
			int n = q.size();
			for (int i = 0; i < n; ++i) {
				string cur = q.front();
				if (cur == target) return step;
				q.pop();
				move(cur, used, deadendset, q);
			}
			step++;
		}
		return -1;
	}
};


int main()
{
	Solution sol;
	// SolutionBFS sol;
	vector<string> deadends{ "0201", "0101", "0102", "1212", "2002" };
	string target("0202");
	int ret = sol.openLock(deadends, target);
	std::cout << ret << "\n";
	system("pause");
	return 0;
}
