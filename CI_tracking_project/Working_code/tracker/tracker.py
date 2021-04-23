import math

class init_tracker:
    def __init__(self,pop_num,frames):
        # Store the center positions of the objects
        self.center_points = {}

        #  A list with numbers 1-pop_num
        self.population_id_list = list(range(0, pop_num))

        # Dictionary to store lost id's
        self.lost_id = {}

        # the number of frames the object is allowed to disappear
        self.frames = frames

    def update(self, objects_rect):

        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            same_object_detected = False
            lost_retrieved = False

            # Checking to see if the new bject is in the same spot as one of the lost objects
            for id, centerp in self.lost_id.items():
                cxl, cyl = centerp[0]
                dist = math.hypot(cx - cxl, cy - cyl)
                if dist < 20:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    self.lost_id.pop(id, None)
                    lost_retrieved = True
                    break


            # Find out if that object was detected already
            print(self.center_points)
            if lost_retrieved is False:

                for id, pt in self.center_points.items():
                    dist = math.hypot(cx - pt[0], cy - pt[1])

                    ### change distance if id increase from flicker is detected
                    if dist < 20:
                        self.center_points[id] = (cx, cy)
                        #print(self.center_points)
                        objects_bbs_ids.append([x, y, w, h, id])
                        same_object_detected = True
                        break


            # New object is detected we assign the ID to that object
            if same_object_detected is False and lost_retrieved is False:
                self.center_points[self.population_id_list[0]] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.population_id_list[0]])
                self.population_id_list.pop(0)

        # Clean the dictionary by center points to remove IDS not used anymore
        new_center_points = {}
        #self.population_id_list = (range(1, pop_num))
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center


        # Adding lost id's to population id array.
        for key in self.center_points.keys():

            if key not in new_center_points.keys():
                self.population_id_list.append(key)
                self.lost_id[key] = (self.center_points[key], 0)

        # Counting up frames that the id has been lost
        for keys in self.lost_id.keys():
            self.lost_id[keys] = (self.lost_id[keys][0], self.lost_id[keys][1]+1)

        # Removing and appending lost id's
        clear_ids = list()
        for p in self.lost_id.keys():

            if self.lost_id[p][1] > self.frames:
                clear_ids.append(p)

        for x in clear_ids:
            self.lost_id.pop(x,None)
            self.population_id_list.append(x)


        self.center_points = new_center_points.copy()


        return objects_bbs_ids
