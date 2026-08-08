#include <stdio.h>
#define MAX_PROCESSES 10
typedef struct {
    int at; 
    int bt; 
    int wt; 
    int tat; 
} Process;
void fcfs(Process p[], int n) {
    int total_wt = 0, total_tat = 0;
    int i, j;
    for (i = 0; i < n; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (p[j].at > p[j + 1].at) {
                Process temp = p[j];
                p[j] = p[j + 1];
                p[j + 1] = temp;
            }
        }
    }
    p[0].wt = 0;
    p[0].tat = p[0].bt;
    for (i = 1; i < n; i++) {
        p[i].wt = p[i - 1].bt + p[i - 1].wt;
        p[i].tat = p[i].wt + p[i].bt;
        total_wt += p[i].wt;
        total_tat += p[i].tat;
    }
    printf("Process Name | Burst Time (bt) | Arrival Time (at) | Waiting Time (wt) | Turnaround Time |\n");
    for (i = 0; i < n; i++) {
        printf("%s%11d | %11d | %13d | %14d |\n", "p", p[i].bt, p[i].at, p[i].wt, p[i].tat);
    }
    printf("\nAverage Waiting Time = %.2f\n", (float)total_wt / n);
    printf("Average Turnaround Time = %.2f\n", (float)total_tat / n);
    printf("\nGANTT CHART:\n");
    int time = 0;
    for (i = 0; i < n; i++) {
        for (j = p[i].at; j < p[i].at + p[i].bt; j++) {
            printf("%d ", j);
        }
        time = p[i].at + p[i].bt;
    }
    printf("\n");
}
int main() {
    Process p[MAX_PROCESSES];
    int n;
    printf("Enter the number of processes: ");
    scanf("%d", &n);
    printf("Enter Arrival Time and Burst Time for each process:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d%d", &p[i].at, &p[i].bt);
    }
    fcfs(p, n);
    return 0;
}