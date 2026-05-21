class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_rows = len(board)
        num_cols = num_rows
        num_boxes = num_rows

        rows = {row:[] for row in range(num_rows)}
        cols = {col:[] for col in range(num_cols)}
        boxes = {box:[] for box in range(num_boxes)}

        for r in range(num_rows):
            for c in range(num_cols):
                value = board[r][c]

                if value == '.':
                    continue

                if value in rows[r]:
                    return False
                else:
                    rows[r].append(value)
                
                if value in cols[c]:
                    return False
                else:
                    cols[c].append(value)
                
                box_index = (r // 3) * 3  + (c // 3) 
                if value in boxes[box_index]:
                    return False
                else:
                    boxes[box_index].append(value)
        
        return True
        