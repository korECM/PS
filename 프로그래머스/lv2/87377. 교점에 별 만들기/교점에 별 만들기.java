import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        Line[] lines = new Line[line.length];
        for(int i = 0; i < line.length; i++){
            int[] e = line[i];
            lines[i] = new Line(e[0], e[1], e[2]);
        }
        List<Point> points = getIntersections(lines);
        
        Point minPoint = getMinPoint(points);
        Point maxPoint = getMaxPoint(points);
        
        int width = (int)(maxPoint.x - minPoint.x)+ 1;
        int height = (int)(maxPoint.y - minPoint.y) + 1;
        
        char[][] boards = new char[height][width];
        for(char[] row : boards){
            Arrays.fill(row, '.');
        }
        
        for(Point p : points) {
            int x = (int)(p.x - minPoint.x);
            int y = (int)(maxPoint.y - p.y);
            boards[y][x] = '*';
        }
        
        String[] answer = new String[height];
        
        for(int i = 0; i < height; i++){
            answer[i] = new String(boards[i]);
        }
        
        return answer;
    }
    
    private long abs(long n){
        return n > 0 ? n : -n;
    }
    
    private List<Point> getIntersections(Line[] lines) {
        List<Point> points = new ArrayList<>();
        for(int i = 0; i < lines.length; i++){
            for(int j = i; j < lines.length; j++){
                Point intersection = lines[i].getIntersection(lines[j]);
                if(intersection != null) {
                    points.add(intersection);
                }
            }
        }
        return points;
    }
    
    private Point getMinPoint(List<Point> points){
        long minX = Long.MAX_VALUE;
        long minY = Long.MAX_VALUE;
        
        for(Point p : points){
            if(p.x < minX) minX = p.x;
            if(p.y < minY) minY = p.y;
        }
        return new Point(minX, minY);
    }
    
    private Point getMaxPoint(List<Point> points) {
        long maxX = Long.MIN_VALUE;
        long maxY = Long.MIN_VALUE;
        
        for(Point p : points){
            if(p.x > maxX) maxX = p.x;
            if(p.y > maxY) maxY = p.y;
        }
        return new Point(maxX, maxY);
    }
}

class Line {
    private final long a;
    private final long b;
    private final long e;
    Line(long a, long b, long e) {
        this.a = a;
        this.b = b;
        this.e = e;
    }
    
    Point getIntersection(Line line){
        long c = line.a;
        long d = line.b;
        long f = line.e;
        double x = (double)(b * f - e * d) / (a * d - b * c);
        double y = (double)(e * c - a * f) / (a * d - b * c);
        if (Double.isNaN(x) || Double.isNaN(y)) {
            return null;
        }
        if (x % 1 != 0 || y % 1 != 0) { return null; }
        return new Point((long)x, (long)y);
    }
}

class Point {
    final long x;
    final long y;
    Point(long x, long y){
        this.x = x;
        this.y = y;
    }
    
    public String toString() {
        return "Point[x=" + x + ", y=" + y + "]";
    }
}