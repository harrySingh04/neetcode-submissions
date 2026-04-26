class DynamicArray {

    int[] dynArray;
    int capacity;
    int currIdx;

    public DynamicArray(int capacity) {

        this.capacity = capacity;
        this.dynArray = new int[capacity];
        currIdx = 0;

    }

    public int get(int i) {
        return dynArray[i];
    }

    public void set(int i, int n) {
        dynArray[i] = n;
    }

    public void pushback(int n) {

        if(this.currIdx == this.capacity){
            resize();
        }
        this.dynArray[currIdx] = n;
        currIdx++;
    }

    public int popback() {
        if(currIdx > 0){
            currIdx--;
        }
        return this.dynArray[currIdx];
    }

    private void resize() {
        this.capacity = 2 * capacity;
        int[] newArray = new int[this.capacity];
        for(int i=0;i<currIdx;i++){
            newArray[i] = this.dynArray[i];
        }
        this.dynArray = newArray;
        
    }

    public int getSize() {
        return this.currIdx;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
