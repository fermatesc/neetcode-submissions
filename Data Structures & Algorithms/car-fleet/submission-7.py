class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        steps = [] 
        for pos, sp in cars:
            st = (target - pos)/sp
            if not steps or st > steps[-1]:
                steps.append(st)
        
        return len(steps)
