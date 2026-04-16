from pathlib import Path
from typing import List
from dataclasses import dataclass
from collections import defaultdict
import re

@dataclass
class FlightFiles:
    flight_id: str
    sp2: str
    ams: str
    core: str
    core_cloud: str
    neph: str
    summary: str

def collect_files(base_dir: str, dirs: List[str], subpath: str, pattern: str, exclude: str = None) -> List[str]:
    all_files = []

    for d in dirs:
        search_dir = Path(base_dir) / d / subpath
        files = sorted(search_dir.glob(pattern))

        if exclude:
            files = [f for f in files if exclude not in f.name]

        all_files.extend([str(f) for f in files])

    return all_files

def extract_flight_number(file_path: str) -> str:
    match = re.search(r'b\d{3}', file_path)
    return match.group(0) if match else None


def get_matched_flights(base_dir: str, dirs: list) -> list[FlightFiles]:
    """
    Returns a list of FlightFiles with all required datasets matched by flight ID.
    """

    # --- Collect files ---
    core_processed_files = collect_files(base_dir, dirs, "core_processed", "core_faam*r1*.nc", exclude="_1hz")
    dry_neph_files = collect_files(base_dir, dirs, "mo-non-core", "metoffice*neph1*.nc")
    sp2_files = collect_files(base_dir, dirs, "non-core", "man-sp2*.na")
    ams_files = collect_files(base_dir, dirs, "non-core", "man-ams*.na")
    flight_sum_files = collect_files(base_dir, dirs, ".", "flight-sum*.txt")
    core_processed_files_cloud = collect_files(base_dir, dirs, "core_processed", "core-cloud*r0*.nc")

    # --- Organize by flight ---
    file_maps = {
        "core": core_processed_files,
        "neph": dry_neph_files,
        "sp2": sp2_files,
        "ams": ams_files,
        "summary": flight_sum_files,
        "core_cloud": core_processed_files_cloud,  # Assuming core and core_cloud are the same file
    }

    flights_dict = defaultdict(dict)

    for key, files in file_maps.items():
        for f in files:
            flight_id = extract_flight_number(f)
            if flight_id:
                flights_dict[flight_id][key] = f

    # --- Keep only complete flights ---
    required_keys = {"core", "neph", "sp2", "ams", "summary", "core_cloud"}

    matched_flights = []

    for flight_id, data in flights_dict.items():
        if required_keys.issubset(data.keys()):
            matched_flights.append(
                FlightFiles(
                    flight_id=flight_id,
                    sp2=data["sp2"],
                    ams=data["ams"],
                    core=data["core"],
                    core_cloud=data["core_cloud"],  # Assuming core and core_cloud are the same file
                    neph=data["neph"],
                    summary=data["summary"],
                )
            )

    print(f"Matched flights: {len(matched_flights)}")

    return sorted(matched_flights, key=lambda x: x.flight_id)