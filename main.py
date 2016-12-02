import threads
import math

class RollerScrewMetric:
    """ For designing roller screw linear actuators
        many of the equations come from here:
            http://www.creativemotioncontrol.com/home-copy/cmc-roller-screws/calculation-and-selection/efficiency-and-driving-torque
    """
    def __init__(self):
        pass

    def setMaterial(self, material):
        if isinstance(material, basestring):
            if material=="PLA":
                self.tensileStrengthMPa = 57.8
                #todo: find actual values
                self.frictionCoefficientStatic = 0.35
                self.frictionCoefficientSliding = 0.3
                self.frictionCoefficientSlidingLubricated = 0.07
                #todo: adjust this once experiment 1 finished
                self.frictionCoefficientRollingPerMM=0.00177
            elif material == "ABS":
                self.tensileStrengthMPa = 44.81
                # todo: find actual values
                self.frictionCoefficientStatic = 0.35
                self.frictionCoefficientSliding = 0.3
                self.frictionCoefficientSlidingLubricated = 0.07
                self.frictionCoefficientRollingPerMM = 0.00177
            elif material == "Aluminum 6061-T6" or "6061-T651" or "Aluminum":
                self.tensileStrengthMPa = 276 #yield strength for metals
                self.frictionCoefficientStatic = 0.35
                self.frictionCoefficientSliding = 0.3
                self.frictionCoefficientSlidingLubricated = 0.07
                # todo: find actual values or make a calculator
                self.frictionCoefficientRollingPerMM = 0.000866

    def getTheoreticalDriveEfficiency(self):
        inner_avg_max_diam = (self.innerThread.major_diameter_max + self.innerThread.minor_diameter_max) / 2
        inner_avg_min_diam = (self.innerThread.major_diameter_min + self.innerThread.minor_diameter_min) / 2
        inner_avg_diam = (inner_avg_max_diam + inner_avg_min_diam) / 2

        rolling_resistance_coefficient = (self.frictionCoefficientRollingPerMM) * inner_avg_diam

        efficiency = 1/(1+((math.pi*inner_avg_diam)/(self.innerThread.pitch+self.outerThread.pitch*
                                                     (self.innerThread.diameter/self.outerThread.diameter)))*
                        rolling_resistance_coefficient)
        return efficiency

    def getTheoreticalBackdriveEfficiency(self):
        efficiency = self.getTheoreticalDriveEfficiency()
        backdrive_efficiency = 2- 1 / efficiency
        return backdrive_efficiency

    def getPracticalDriveEfficiency(self):
        efficiency = self.getTheoreticalDriveEfficiency()
        return efficiency*.9

    def getPracticalBackdriveEfficiency(self):
        efficiency = self.getTheoreticalBackdriveEfficiency()
        return efficiency * .9

    def getTorqueRequiredToMoveAxialLoad(self, loadKg):
        torque = ((loadKg*9.8)*self.innerThread.pitch)/ \
                 (2*math.pi*self.getPracticalDriveEfficiency() * 10**3)
        return torque

    def getMaxAxialLoadKgForTorque(self, Nm):
        axial_load_newtons = (Nm*(2*math.pi*self.getPracticalDriveEfficiency() * 10**3)) / self.innerThread.pitch
        axial_load_kilograms = axial_load_newtons/9.8
        return axial_load_kilograms

    def setInnerThread(self, thread_class, diameter, pitch):
        self.innerThread = threads.thread[thread_class][diameter][pitch]

    def setOuterThread(self,  thread_class, diameter, pitch):
        self.outerThread = threads.thread[thread_class][diameter][pitch]

    def setMotor(self, torqueNm, speedRPM):
        self.motorNm=torqueNm
        self.motorRPM = speedRPM

    def getAxialSpeed(self, rpm):
        speed = (rpm/60.0)*self.innerThread.pitch/(10)
        return speed #cm/sec

    def getAxialKgGivenDesiredSpeed(self, cmps):
        desired_rpm = cmps*10.0*60.0/self.innerThread.pitch
        multiplier = float(self.motorRPM) / desired_rpm
        print("m: "+str(multiplier))
        return self.getMaxAxialLoadKgForTorque(self.motorNm*multiplier)

def motorFromAmpsVoltsKv(amps, volts, kv):
    watts = volts*amps
    rpm = kv*volts
    print rpm
    #from here: http://www.engineeringtoolbox.com/electrical-motors-hp-torque-rpm-d_1503.html
    newton_meters = watts*9.549 / rpm
    print newton_meters

if __name__ == "__main__":
    motorFromAmpsVoltsKv(135, 15, 5400)

    roller_screw = RollerScrewMetric()
    roller_screw.setMaterial("PLA")
    roller_screw.setInnerThread("6g", 18, 1)
    #to connect best, 'roller' screws should have same handedness and pitch
    roller_screw.setOuterThread("6g", 6, 1)

    print(roller_screw.getTorqueRequiredToMoveAxialLoad(1))
    print(roller_screw.getMaxAxialLoadKgForTorque(0.238725))

    roller_screw.setMotor(0.238725, 81000)

    print(roller_screw.getAxialKgGivenDesiredSpeed(30))
