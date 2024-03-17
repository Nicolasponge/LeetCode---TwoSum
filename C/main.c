/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *indices = (int*)malloc(2 * sizeof(int));
    if (indices == NULL) {
        *returnSize = 0;
        return NULL;
    } // Caso não tenha memória suficiente ele para a execução, um erro, NULL
    
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                indices[0] = i;
                indices[1] = j;
                *returnSize = 2;
                return indices;
            }
        }
    }
    
    *returnSize = 0;
    free(indices);
    return NULL; // Nenhuma solução foi encontrada
}
