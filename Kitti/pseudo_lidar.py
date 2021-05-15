import argparse
import os

"""
Original KITTI dataset folder looks like:
    training
        calib
        image_2
        label_2
    testing
        calib
        image_2
    train.txt
    val.txt
    trainval.txt
    test.txt
"""

parser = argparse.ArgumentParser()
parser.add_argument('--data_path', type=str, default='~/KITTI/object/', help='path to the kitti dataset')
parser.add_argument('--train_velodyne', type=str, help='path to the training velodyne')
parser.add_argument('--train_planes', type=str, help='path to the training planes')
parser.add_argument('--test_velodyne', type=str, help='path to the testing velodyne')
parser.add_argument('--test_planes', type=str, help='path to the testing planes')
parser.add_argument('--save_name', type=str, help='name of the target folder')
args = parser.parse_args()


def main():
    os.makedirs(args.save_name + '/training', exist_ok=True)
    os.makedirs(args.save_name + '/testing', exist_ok=True)
    for folder in ['calib', 'image_2', 'label_2']:
        assert os.path.isdir(args.data_path + '/training/{}'.format(folder))
        os.system('ln -s {0}/training/{2} {1}/training/{2}'.format(args.data_path, args.save_name, folder))
    for folder in ['calib', 'image_2']:
        assert os.path.isdir(args.data_path + '/testing/{}'.format(folder))
        os.system('ln -s {0}/testing/{2} {1}/testing/{2}'.format(args.data_path, args.save_name, folder))
    for f in ['train.txt', 'val.txt', 'trainval.txt', 'test.txt']:
        os.system('cp official_split/{1} {0}/{1}'.format(args.save_name, f))

    assert os.path.isdir(args.train_velodyne)
    os.system('ln -s {0} {1}/training/velodyne'.format(args.train_velodyne, args.save_name))
    assert os.path.isdir(args.train_planes)
    os.system('ln -s {0} {1}/training/planes'.format(args.train_planes, args.save_name))

    assert os.path.isdir(args.test_velodyne)
    os.system('ln -s {0} {1}/testing/velodyne'.format(args.test_velodyne, args.save_name))
    assert os.path.isdir(args.train_planes)
    os.system('ln -s {0} {1}/testing/planes'.format(args.test_planes, args.save_name))


if __name__ == '__main__':
    main()
