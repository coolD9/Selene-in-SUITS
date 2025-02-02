## UI Requirements

The following requirements are organized based on `shall`, `should`, and `may`, as per the mission description requirements for the rover, __only pertaining to the User Interface portions__. They will be accompanied with a scale from `P0` - `P4`, where `P0` is the highest priority and `P4` is the lowest priority **within the respective category, NOT OVERALL**. 
These priority levels will help determine what tasks should be accomplished first within that category. Please note priorities are prone to changing based on team confidence in subjects. I personally made the decision to mark some tasks with `CR` for "Communication Required", which will require coordination with UCI to determine how exactly we want to interface with their data.

**Note:** Section 7 and 8 of the requirements page are for the Autonomous parts of the PR.

### Shall
As a reminder, `Shall` denotes a minimum requirement for the functionality of the UI, all of these **must** be accomplished before our final submission and accomplished before any other section.

- [ ] __P0:__ *Shall* develop system for controlling the rover in the virtual DUST environment.
- [ ]  __P1:__ The UI *Shall* display crewmember biomedical data. This data *shall* be easily accessible.
- [ ]  __CR:__ The UI *shall* display spacesuit system state data. This data *shall* be easily accessible.
     *  Note: The data will come from your partnered team, we must coordinate with them to figure out what form this data will come in.
- [ ]  __P2:__ The UI *shall* display the Lunar Terrain Vehicle (LTV) native camera feed.
- [ ]  __P1:__ The UI *shall* display the LTV telemetry. This data *shall* be easily accessible.
- [ ]  __P2:__ The UI *shall* display procedures for tasks. All procedures shall be easily accessible.
- [ ]  __CR:__ The UI *shall* display X-Ray Fluorescence sensor data when the data has been collected by the EV in the field.
- [ ]  __P2:__ The UI *shall* include a live 2D map for tracking human and scientific assets.
     - [ ] __P3:__ The map *shall* track crewmembers' locations live for the duration of the EVA.
- [ ] __P3:__ The map *shall* track the LTV's location for the duration of the EVA.
- [ ] __P3:__ The map *shall* display all designated points of interest.
- [ ] __P3:__ The map *shall* update to show any added points of interest by the EV or PR.
- [ ] __P3:__ The map *shall* allow the user to add points of interest and share with EV.
- [ ] __P4:__ The UI *shall* implement feature for dropping pins on map.
- [ ] __CR:__ Dropped pins *shall* sync across interfaces (PR, EV).
- [ ] __P2:__ The UI *shall* feature a caution and warning system.
     - [ ] __P2:__ The caution and warning system *shall* alert PR when any telemetry enter off-nominal ranges.
- [ ] __P3:__ The UI *shall* display the mission elapsed time.
- [ ] __P3:__ The UI *shall* display the elapsed time at each station throughout the EVA.
     - [ ] __P4:__ All mission timers *shall* adhere to standards and constrains provided to selected teams.

### Should
The `Should` requirements are listed as secondary priority. Not strictly necessary for a minimal viable product, but definitely preferred.

- [ ]  __P1:__ The UI *should* display crewmember camera feed.
- [ ]  __P2:__ The map pin labels *should* be customizable.

### May
The Mission Description states that items listed with `may` are optional goals for development. This implies that they have extremely low priority and can be tackled if we have excess time.

- [ ] __P1:__ The map *may* draw the LTV's projected and traversed path.
- [ ] __P2:__ The map *may* draw the EV's projected and traversed path.
- [ ] __P3:__ Teams *may* store XRF data for recall
