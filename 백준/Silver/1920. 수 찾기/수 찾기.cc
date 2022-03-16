#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
int arr[1000010];

void BinarySearch(int *arr, int x)
{
	int start = 0, end = N-1, mid = (start + end) / 2;
	while (start <= end)
	{
		if (arr[mid] == x)
		{
			std::cout << "1" << "\n";
			return;
		}
		else if (x < arr[mid])
		{
			end = mid - 1;
		}
		else
			start = mid + 1;
		mid = (start + end) / 2;
	}
	std::cout << "0" << "\n";
}



int main()
{
	int x;
    ios_base::sync_with_stdio(0);
	cin.tie(0);

	std::cin >> N;

	for (int i = 0; i < N; i++)
	{
		std::cin >> x;
		arr[i] = x;
	}

	sort(arr, arr+N);

	std::cin >> M;
	for (int i = 0; i < M; i++)
	{
		std::cin >> x;
		BinarySearch(arr, x);
	}

	return 0;
}