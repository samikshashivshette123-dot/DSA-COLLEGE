#include <stdio.h>
#include<conio.h>
// Function for Linear Search
int linearSearch(int arr[], int n, int key) {
    int i;
    for (i = 0; i < n; i++) {
	if (arr[i] == key)
	  return i;   // Return index if found
	}
    return -1;          // Return -1 if not found
}

// Function for Binary Search
int binarySearch(int arr[], int low, int high, int key) {
    while (low <= high) {
	int mid = (low + high) / 2;

	if (arr[mid] == key)
	    return mid;
	else if (arr[mid] < key)
	    low = mid + 1;
	else
	    high = mid - 1;
    }
     return -1;          // Return -1 if not found
}

int main() {
    int n, key, i,accountID[100];
 int linearResult, binaryResult;
 clrscr();
    printf("Enter the number of customer account IDs: ");
    scanf("%d", &n);
    printf("Enter the customer account IDs (sorted for Binary Search):\n");
    for (i = 0; i < n; i++) {
	scanf("%d", &accountID[i]);
    }

    printf("Enter the customer account ID to search: ");
    scanf("%d", &key);

    linearResult = linearSearch(accountID, n, key);
    if (linearResult != -1)
	printf("\nLinear Search: Customer Account ID found at position %d.\n", linearResult + 1);
    else
	printf("\nLinear Search: Customer Account ID not found.\n");



    binaryResult = binarySearch(accountID, 0, n - 1, key);
    if (binaryResult != -1)
	printf("Binary Search: Customer Account ID found at position %d.\n", binaryResult + 1);
    else
	printf("Binary Search: Customer Account ID not found.\n");
    getch();
    return 0;
}