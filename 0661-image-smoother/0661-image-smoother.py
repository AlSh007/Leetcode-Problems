class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Save the dimensions of the image.
        m = len(img)
        n = len(img[0])

        # Iterate over the cells of the image.
        for i in range(m):
            for j in range(n):
                # Initialize the sum and count 
                sum = 0
                count = 0

                # Iterate over all plausible nine indices.
                for x in (i - 1, i, i + 1):
                    for y in (j - 1, j, j + 1):
                        # If the indices form valid neighbor
                        if 0 <= x < m and 0 <= y < n:
                            # Extract the original value of img[x][y].
                            sum += img[x][y] & 255
                            count += 1
                
                # Encode the smoothed value in img[i][j].
                img[i][j] |= (sum // count) << 8
        
        # Extract the smoothed value from encoded img[i][j].
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8
            
        # Return the smooth image.
        return img